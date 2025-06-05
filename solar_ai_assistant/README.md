# Solar Rooftop Potential Analyzer - Project Documentation

## 📌 Project Title

**AI-Based Rooftop Solar Analysis Tool**

## 🎯 Objective

The idea behind this project is to make it easier for homeowners and solar professionals to understand how suitable a rooftop is for installing solar panels—just by uploading a satellite image. The tool calculates usable area, potential installation capacity, and even estimates the ROI (Return on Investment).

---

## Live link :- 





## 🧱 Project Structure (Simple & Modular)

```
solar_ai_assistant/
├── app.py                    # Streamlit user interface
├── requirements.txt         # All necessary Python packages
└── utils/
    ├── __init__.py          # Makes 'utils' a module
    └── solar_analysis.py    # Core logic for area & ROI estimation
```

---

## ⚙️ How to Set It Up (Step-by-Step)

1. Download the project folder or clone it from GitHub
2. Open your terminal or VS Code inside the folder
3. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
streamlit run app.py
```

That’s it! You’ll see the Streamlit web app open in your browser.

---

## 🔧 How the Tool Works

1. **Upload an Image** – A clear rooftop image (top view) is uploaded by the user.
2. **Area Estimation** – The tool simulates analysis using simple logic to calculate the usable area on the rooftop.
3. **Panel Fitting** – It estimates how many standard-sized solar panels can fit based on the area.
4. **ROI & Cost** – The tool calculates total installation cost, subsidy, and how long it will take to recover the investment.
5. **Result Displayed** – Everything is shown clearly through the web interface.

---

## 🔍 Example Use Case

Let’s say the user uploads a rooftop image that roughly covers 1000 sq ft.

The output could look like:

* Rooftop Area Detected: 1000 sq ft
* Approx. 50 panels can fit
* Estimated Installation Cost: ₹2,50,000
* Govt Subsidy: ₹75,000
* Net Cost: ₹1,75,000
* ROI: \~3.5 years

(Note: These values are based on assumptions and a fixed panel size in the code.)

---

## 🚀 What Can Be Improved Next?

Here are some realistic next steps and ideas for future upgrades:

1. **Real AI Integration** – Integrate LLMs or vision models like GPT-4o or SAM to process actual satellite images.
2. **Better Image Analysis** – Use YOLO or semantic segmentation to accurately detect usable roof area.
3. **More Context** – Add APIs to fetch local electricity rates, location-based sunlight hours, etc.
4. **Confidence Score** – Show how confident the system is in its predictions.
5. **Convert to API** – Make this a backend service using FastAPI so it can be used in mobile or web apps.
6. **Performance Metrics** – Log things like average analysis time, success rate, etc.
7. **Mobile Friendly** – Turn this into a mobile app or responsive web tool.

---

## ✅ In Summary

This project is a good starting point for building smarter solar planning tools. While the current version uses simulated logic, it sets the stage for integrating real AI vision tools and expanding into a full-fledged product.

It’s simple, clean, and easy to use—which is what we were aiming for. 😄

---

📌 *Prepared as part of an internship technical assessment for a solar industry AI assistant.*

