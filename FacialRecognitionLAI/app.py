from PIL import Image
from landingai.predict import Predictor
# Enter your API Key
endpoint_id = "528faa51-ccb0-4354-9580-c3ab2169a7b1"
api_key = "land_sk_363nFQRJgOBhQ7rLZEeT8uL4D3m4xi1NOcAa5FoqzhqVjLelty"
# Load your image
image = Image.open("C:/Users/hp/Documents/GitHub/MinorProjects-ML/Front_View.jpg")
# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)