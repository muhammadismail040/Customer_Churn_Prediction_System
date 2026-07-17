import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("=" * 60)
print("ENV API KEY:", API_KEY)
print("=" * 60)

api_key_header = APIKeyHeader(
    name="x-api-key",
    auto_error=False,
)


def verify_api_key(
    api_key: str = Security(api_key_header),
):
    print("=" * 60)
    print("HEADER API KEY :", api_key)
    print("ENV API KEY    :", API_KEY)
    print("=" * 60)

    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key is missing.",
        )

    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key.",
        )

    return api_key