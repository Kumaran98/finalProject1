# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:32:01 2022

@author: Eelapriya
"""

from fastapi import FastAPI
import uvicorn
import pickle

from models import Women
app=FastAPI()
model = pickle.load(open("model_rf.pkl","rb"))
@app.get("/")
def greet():
   return{"Hello World"}

@app.post("/predict")
def predict(req:Women):
   Customer_Age = req.Customer_Age       
   Gender     = req.Gender                   
   Dependent_count = req.Dependent_count        
   Months_on_book = req.Months_on_book      
   Total_Relationship_Count = req.Total_Relationship_Count        
   Months_Inactive_12_mon  = req.Months_Inactive_12_mon   
   Contacts_Count_12_mon  = req.Contacts_Count_12_mon        
   Credit_Limit    = req.Credit_Limit                        
   Total_Revolving_Bal  =  req.Total_Revolving_Bal              
   Avg_Open_To_Buy = req.Avg_Open_To_Buy                   
   Total_Amt_Chng_Q4_Q1   = req.Total_Amt_Chng_Q4_Q1       
   Total_Trans_Amt   = req.Total_Trans_Amt               
   Total_Trans_Ct     = req.Total_Trans_Ct                   
   Total_Ct_Chng_Q4_Q1 = req.Total_Ct_Chng_Q4_Q1      
   Avg_Utilization_Ratio  = req.Avg_Utilization_Ratio         
   Naive_Bayes_1   = req.Naive_Bayes_1
   Naive_Bayes_2   = req.Naive_Bayes_2
   Doctorate      = req.Doctorate       
   Graduate       = req.Graduate                                
   School     = req.School                       
   PGraduate   = req.PGraduate                    
   Uneducated  = req.Uneducated                           
   Unknown_1 = req.Unknown_1                          
   Married    = req.Married                              
   Single   = req.Single                            
   Unknown_2  = req.Unknown_2                     
   Salary_1 = req.Salary_1                      
   Salary_2  = req.Salary_2                       
   Salary_3  = req.Salary_3               
   Salary_4   = req.Salary_4            
   Unknown_3    = req.Unknown_3                
   Gold   = req.Gold                           
   Platinum = req.Platinum                   
   Silver  = req.Silver   
   features=list([ Customer_Age,Gender,Dependent_count,Months_on_book,
   Total_Relationship_Count,Months_Inactive_12_mon,
   Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,
   Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
   Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio,
   Naive_Bayes_1,Naive_Bayes_2,Doctorate,Graduate,School,
   PGraduate,Uneducated, Unknown_1,Married,Single,Unknown_2,
   Salary_1,Salary_2,Salary_3,Salary_4,Unknown_3, Gold, Platinum,Silver ])      
   predict=model.predict([features])  
   probab = model.predict_proba([features])    
   if(predict ==1):
      return{"ans":"You have been tested positive with this {} Probability".format(probab[0][1])}
   else:
      return{"ans":"You have been Negative positive with this {} Probability".format(probab[0][0])}

if __name__ == "__main__":
  uvicorn.run(app)
