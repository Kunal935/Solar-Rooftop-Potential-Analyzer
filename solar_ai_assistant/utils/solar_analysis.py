from PIL import Image
import numpy as np

def analyze_image_and_estimate(image: Image.Image) -> dict:
    # Resize image to standard size for estimation (simulate AI vision model)
    image = image.resize((300, 300))
    img_array = np.array(image.convert("L"))  # Convert to grayscale

    # Dummy logic to simulate rooftop detection (we count bright areas)
    threshold = 180
    usable_pixels = np.sum(img_array > threshold)
    total_pixels = img_array.size
    usable_ratio = usable_pixels / total_pixels

    # Assume each pixel represents 0.01 m²
    usable_area = round(usable_ratio * 90, 2)  # simulate max 90 m² roof

    # Solar panel specs
    panel_area = 1.6  # m²
    panel_price = 22000  # INR
    panel_capacity = 330  # watts

    panel_count = int(usable_area // panel_area)
    estimated_cost = panel_count * panel_price

    # Monthly savings estimate
    generation_per_panel = 40  # kWh per month
    rate = 7  # ₹/kWh
    monthly_savings = generation_per_panel * rate * panel_count

    # Payback period
    payback_period = round(estimated_cost / monthly_savings, 2) if monthly_savings > 0 else 0

    return {
        "usable_area": usable_area,
        "panel_count": panel_count,
        "estimated_cost": estimated_cost,
        "monthly_savings": int(monthly_savings),
        "payback_period": payback_period
    }
