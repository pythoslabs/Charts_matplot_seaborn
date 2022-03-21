''' 
A function to create simple charts by passing a dataframe 
- creates individual charts based on the values in the dataframe against an x-y combination 

create_combo_chart(string, dataframe)
eg: create_combo_chart(mat_num,df_mat)
Note : For the names in the columns being called in the data frame - make sure these columns are present in the df that you are passing 
'''

# Simple chart
def create_price_chart(img_fname,df):
        #plt_ax = plt.axis('off');  # no numbers on axis - clean graph
       
        plt_1 = plt.plot(df['Quantity], label = "Qty");
        plt_2 = plt.plot(df['Price'], label = "Price");
        # if you want to plot multiple lines, add those plots here
                            
        plt.legend(loc="upper left") # Add legend
        plt.title(mat_num); # Add title
        plt_sav = plt.savefig("../graph_price_var/" +  img_fname + '.jpg' , dpi = 100,format = 'jpeg');
        plt.clf();
        
