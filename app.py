# !pip install gradio ipywidgets
import pandas as pd
import gradio as gr
import joblib

# "Artifacts"
model = joblib.load("model.joblib")
labels = joblib.load("labels.joblib")

def decodeLifeStyle(encodedValue) :
    lifestyle_encoded = {'Eco-Friendly': 1,
 'Adventure Seeker': 2,
 'Urban Professional': 3,
 'Budget-Conscious': 4,
 'Health-Conscious': 5,
 'Tech-Savvy': 6,
 'Social Media Influencer': 7,
 'Sustainable Investor': 8,
 'Digital Nomad': 9,
 'Travel Enthusiast': 10,
 'Fitness Enthusiast': 11,
 'Investor': 12}
    
    for lifestyle, value in lifestyle_encoded.items() :
        if encodedValue == value:
            return lifestyle
    

def predict(age, avg_ent, online_purchases , charity_donations , invest_port , env_awar , lifestyle_balance , ent_eng, invest_risk , eco_cons , time_man):
    sample = dict()

    sample['Age'] = age
    sample['Average Monthly Spend on Entertainment'] = avg_ent
    sample['Number of Online Purchases in Last Month'] = online_purchases
    sample['Number of Charity Donations in Last Year'] = charity_donations
    sample['Investment Portfolio Value'] = invest_port
    sample['Environmental Awareness Rating'] = env_awar
    sample['Lifestyle Balance Score'] = lifestyle_balance
    sample['Entertainment Engagement Factor'] = ent_eng
    sample['Investment Risk Appetite'] = invest_risk
    sample['Eco-Consciousness Metric'] = eco_cons
    sample['Time Management Skill'] = time_man
    

    lifestyle = model.predict(pd.DataFrame([sample]))
    
    return decodeLifeStyle(lifestyle[0])

# https://www.gradio.app/guides
with gr.Blocks() as blocks:
    age = gr.Slider(19,100, label = 'Age')
    avg_ent = gr.Slider(0,370 , label = 'Average Monthly Spend on Entertainment' , info = '(dollars)')
    online_purchases = gr.Slider(0, 300 , label = 'Number of Online Purchases in Last Month')
    charity_donations = gr.Slider(0, 20 , label = 'Number of Charity Donations in Last Year')
    invest_port = gr.Slider(0,1500, label = 'Investment Portfolio Value')
    env_awar = gr.Slider(0,60, label = 'Environmental Awarness Rating')
    lifestyle_balance = gr.Slider(0,100, label = 'Lifestyle Balance Score')
    ent_eng = gr.Slider(0,5 , label = 'Entertainment Engagement Factor' , step = 0.1)
    invest_risk = gr.Slider(0,20, label = 'Investment Risk Appetite' , step = 0.1)
    eco_cons = gr.Slider(0,5 , label = 'Eco-Consciousness Metric' , step = 0.1)
    time_man = gr.Slider(0, 150 , label = 'Time Management Skill')

    lifestyle = gr.Label(label = 'Lifestyle')

    inputs = [age, avg_ent, online_purchases , charity_donations , invest_port , env_awar , lifestyle_balance , ent_eng, invest_risk , eco_cons , time_man]
    outputs = [lifestyle]

    predict_btn = gr.Button("Predict")
    predict_btn.click(predict, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    blocks.launch() # Local machine only
    # blocks.launch(server_name="0.0.0.0") # LAN access to local machine
    # blocks.launch(share=True) # Public access to local machine
