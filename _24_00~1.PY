from urllib.parse import urlparse, unquote

url = "https://www.amazon.com.mx/King-6-8Kg-Chocolate-Ronnie-Coleman/dp/B010V80O6U/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HU8WC4XGEE1P&dib=eyJ2IjoiMSJ9.8zJrbK9-7ryYD1sv6SuB-9kebI1sRsdJjXV1x4TjWurcsuheh1yedYrLZ97__19cY0TZVYDAZT4f6CyDRZFnQm6maMvUhjmJgQc-exONqiJoNdo5s-z8eGnG_oW117HfODYQBkkwA6x7XienYSH-VQRoe5eRAjGv1dBo18eOWoZJKVU8a-mf3o3oDWMUfkud6w2Kb11BHRVnVwfBPp7VL_lqMic8wPUNShVbJqOqY1_IMCLxw_vXsjwIwYmr742mKfK4jHzQQ4BhDdEbQ43-viDFcNJUJ3VgjKp7WaFJCs4.6r3RdcQgrL_awo17kcdqz-ZP9eP4W6equPef6J1Dmlo&dib_tag=se&keywords=king+mass&qid=1709600277&sprefix=king+mass+%2Caps%2C131&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47"

# parse the URL to extract the path
parsed_url = urlparse(url)
path_segments = parsed_url.path.split('/')

# the product title usually follows the domain and is before the product ID ('dp')
# this may vary, so I need to adjust the index accordingly
product_title_segment = path_segments[1] if len(path_segments) > 1 else ''

# URL decode the title segment to convert URL encoded chars back to text
product_title = unquote(product_title_segment)

print(f"Product Title: {product_title}")
