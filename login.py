from kiteconnect import KiteConnect

api_key = "hxoz9zxmk5qj48lk"
api_secret = "g0jb0zt9d0ek6xt0yni5ovcgqcc96vft"

kite = KiteConnect(api_key=api_key)

# Step 1: Generate the login URL and visit it manually to get the request_token
print("Login URL:", kite.login_url())
