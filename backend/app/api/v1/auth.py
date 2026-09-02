from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.auth import Token
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin
from app.schemas.user import UserResponse
from app.security.auth import create_access_token
from app.security.auth import decode_access_token
from app.security.auth import hash_password
from app.security.auth import verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = db.scalar(
        select(User).where(
            User.email == user_data.email
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="A user with this email already exists.",
        )

    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        ),
        role="student",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post(
    "/login",
    response_model=Token,
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = db.scalar(
        select(User).where(
            User.email == user_data.email
        )
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    if not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="This account is inactive.",
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer",
    }


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    user_id = decode_access_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token.",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found.",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="This account is inactive.",
        )

    return user


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user