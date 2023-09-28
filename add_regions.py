import EHB
import pandas as pd
def main():
# x = EHB.get_uds_data(r"C:\Users\Ben\Documents\LPCA\UDS\UDSSummaryReport2018State2Nov2021.xlsx","UDS Summary Report", 2018)
# y = EHB.get_uds_data(r"C:\Users\Ben\Documents\LPCA\UDS\UDSSummaryReport2019State2Nov2021.xlsx","UDS Summary Report", 2019)
# z= EHB.get_uds_data(r"C:\Users\Ben\Documents\LPCA\UDS\UDSSummaryReport2020State2Nov2021.xlsx","UDS Summary Report", 2019)
    UDS = pd.read_excel(r"C:\Users\bnguyen\Documents\LPCA\UDS\UDS_national_2021.xlsx")

    def add_region(x):
        region_10 = ["Alaska","Washington","Oregon","Idaho"]
        region_9 = ["Palau","California","Nevada","Hawaii","Arizona","Marshall Islands", "American Samoa","Fed.States of Micronesia","Northern Mariana Islands","Guam"]
        region_8 = ["Montana","North Dakota", "South Dakota", "Wyoming", "Utah", "Colorado"]
        region_7 = ["Nebraska","Kansas","Missouri","Iowa"]
        region_6 = ["New Mexico","Oklahoma","Texas","Arkansas","Louisiana"]
        region_5 = ["Minnesota", "Wyoming", "Illinois", "Michigan", "Indiana","Ohio", "Wisconsin"]
        region_4 = ["Mississippi", "Alabama", "Georgia","Florida","Tennessee","Kentucky","South Carolina","North Carolina"]
        region_3 = ["Pennsylvania", "Virginia","West Virginia","Maryland","Delaware", "District of Columbia"]
        region_2 = ["New York","New Jersey","Puerto Rico","Virgin Islands"]
        region_1 = ["Connecticut", "Maine","Vermont","Massachusetts","New Hampshire","Rhode Island"]
        
        # if x in region_10:
        #   return "Region 10"
        if x in region_10:
            return "Region 10"

        elif x in region_9:
            return"Region 9"
        elif x in region_8:
            return"Region 8"
        elif x in region_7:
            return"Region 7"
        elif x in region_6:
            return"Region 6"
        elif x in region_5:
            return"Region 5"
        elif x in region_4:
            return"Region 4"
        elif x in region_3:
            return"Region 3"
        elif x in region_2:
            return"Region 2"
        elif x in region_1:
            return"Region 1"
        else: 
            return "other"  
     
        # print(x)
        # print(y)
    UDS["Region"] = UDS["State"].apply(add_region)
        # a = EHB.combine_dataframes(x[0],y[0])
        # print(a)
        # print(a[0])
        # print(a[1])
        # EHB.to_excel(x,"2018_uds.xlsx")

        # EHB.to_excel(y,"2019_uds.xlsx")
    EHB.to_excel(UDS,"UDS_national_2021.xlsx")
main()