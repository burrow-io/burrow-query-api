# security.py
from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader
from config import settings

# Define the security scheme for Swagger UI
api_key_header = APIKeyHeader(name="x-api-token", auto_error=False)

async def verify_api_token(api_token: str = Security(api_key_header)):
    """
    Verify the API token from the x-api-token header.
    This also makes Swagger UI show an Authorize button.
    """
    if not settings.api_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API token not configured on server",
        )

    if not api_token or api_token != settings.api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API token",
        )

    return True
