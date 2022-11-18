from pydantic import BaseModel

class Women(BaseModel):
    Customer_Age            :   int
    Gender   :                    int
    Dependent_count :             int
    Months_on_book   :          int
    Total_Relationship_Count :         int
    Months_Inactive_12_mon    :     int
    Contacts_Count_12_mon      :      int
    Credit_Limit                :                float
    Total_Revolving_Bal          :         int
    Avg_Open_To_Buy               :        float
    Total_Amt_Chng_Q4_Q1           :    float
    Total_Trans_Amt                 :         int
    Total_Trans_Ct                 :           int
    Total_Ct_Chng_Q4_Q1          :  float
    Avg_Utilization_Ratio         :             float
    Naive_Bayes_1 :    float
    Naive_Bayes_2  :    float
    Doctorate   :                                  int
    Graduate     :                                int
    School   :                               int
    PGraduate  :                             int
    Uneducated :                                 int
    Unknown_1     :                                 int
    Married      :                                      int
    Single        :                                     int
    Unknown_2      :                               int
    Salary_1 :                                   int
    Salary_2 :                         int
    Salary_3 :                            int
    Salary_4 :                        int
    Unknown_3 :                                 int
    Gold   :                                      int
    Platinum :                               int
    Silver    :                               int