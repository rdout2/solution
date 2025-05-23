from flask import current_app

def get_clerk_public_key():
    import requests
    jwks_url = current_app.config["CLERK_JWT_PUBLIC_KEY_URL"]
    jwks = requests.get(jwks_url).json()
    return jwks['keys'][0]

def get_clerk_user_id_from_token(token):
    from jose import jwt
    public_key = get_clerk_public_key()
    try:
        payload = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            audience=current_app.config["CLERK_JWT_AUDIENCE"],
            issuer=current_app.config["CLERK_JWT_ISSUER"]
        )
        return payload.get('sub')
    except Exception as e:
        print("JWT decode error:", e)
        return None
