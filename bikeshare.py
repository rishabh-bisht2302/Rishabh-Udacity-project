# External sources used
#      --> https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#      --> http://unicode.org/emoji/charts/emoji-list.html#1f92d 
#      --> https://www.geeksforgeeks.org/python-program-to-print-emojis/
import time
import numpy as np
import pandas as pd
def get_filters():    
    """
    Asks user to specify a city, month, and day to analyze.

    Input: Function takes nothing and returns a tuple.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Asks the user to enter the name of city for which they want to explore the data.
    # A while loop is used to make sure that the cityname entered is correct and if not,user is asked again to enter the correct city name.
    # An emoji is also used source for which is provided at top.
    city_name = input('Enter the city name to start exploring(CHICAGO / WASHINGTON / NEW YORK CITY) : ')
    while city_name.lower() not in ('chicago','washington','new york city'):
        city_name = input('OOPS..!!\U0001F605   Please type CITY NAME from (CHICAGO / WASHINGTON / NEW YORK CITY)..!! Lets start again.')

    # Asks the user to enter the month of year for which they want to explore the data.
    # A while loop is used to make sure that the month name entered is correct and if not,user is asked again to enter the correct month name. 
    month_name = input('looking for a particular month or for all months,type(\'all\') ? Enter the name of month or type \'all\' for no filter(in words) : ')
    while month_name.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        month_name = input('OOPS..!!\U0001F605   Please type correct MONTH NAME..!! Enter again.')
            
    # Asks the user to enter the month of year for which they want to explore the data.
    # A while loop is used to make sure that the month name entered is correct and if not,user is asked again to enter the correct month name. 
    day = input('For a particular day or all days(\'all\' for all days) ? Enter response(in words) : ')
    while day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        day = input('OOPS..!!\U0001F605   Please enter correct DAY (eg. \'sunday\'). Enter again.')
    print('\n'*2)

    # Function returns the tuple of strings.
    return city_name.lower(),month_name.lower(),day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Converting the name of month to respective integer representation.
    date = {'januray':1,'february':2,'march':3,'april':4,'may':5,'june':6}
    for key,value in date.items():
        if key == month.lower():
            req_month = value

    # Reads the csv file for city entered by user and creates a DataFrame.
    file = pd.read_csv(city.replace(' ','_').lower() + '.csv')
    
    # Replacing the Null values with zeros in the DataFrame
    file = file.fillna(0)

    # Converting Start time to datetime format and creating additional columns to apply filter to the DataFrame.
    file['Start Time'] = pd.to_datetime(file['Start Time'])
    file['Week_day'] = file['Start Time'].dt.weekday_name
    file['Month'] = file['Start Time'].dt.month
    file['Hours'] = file['Start Time'].dt.hour

    # Filtering the data from DataFrame.
    if month != 'all':
        file = file[file['Month'] == req_month] 
    if day != 'all':
        file = file[file['Week_day'] == day.title()]

    # Filtered DataFrame is returned.
    return file

def time_stats(df,month,day):
    """ Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    # Marking time as start time in order to calculate the time taken by function to execute.
    start_time = time.time()

    # Checks if the the filter is applied for month or not.If yes,the function doesnt print the most popular month.
    if month == 'all':

        # Counts the number of times an unique value appears in the 'Month' column and picks up the maximum of those.
        most_pop_month_count = df['Month'].value_counts().max()  

        # Picks up the value which appears most frequently in the 'Month' column.
        most_pop_month = df['Month'].mode()[0]

        # Converting the integer representation of month to respective name of month
        date = np.array(['Januray','February','March','April','May','June'])
        most_pop_month_new = date[most_pop_month-1]
        print('Most popular month :',most_pop_month_new,'\tcount :',most_pop_month_count)

    # Checks if the the filter is applied for day of week or not.If yes,the function doesnt print the most popular day of week.
    if day == 'all':

        # Counts the number of times an unique value appears in the 'Week_day' column and picks up the maximum of those.
        most_pop_weekday_count = df['Week_day'].value_counts().max()
        
        # Picks up the value which appears most frequently in the 'Week_day' column.
        most_pop_weekday = df['Week_day'].mode()[0]
        print('Most popular weekday :',most_pop_weekday,'\tcount :',most_pop_weekday_count)
    
    # Counts the number of times an unique value appears in the 'Hours' column and picks up the maximum of those.
    most_pop_hour_count = df['Hours'].value_counts().max()
    
    # Picks up the value which appears most frequently in the 'Hours' column.
    most_pop_hour = df['Hours'].mode()[0]
    print('Most popular hour :',most_pop_hour,'\tcount :',most_pop_hour_count)

    # Marking the time as end time for calculation of time taken for execution of above code.
    print("\nThis took {} seconds.".format(time.time() - start_time))
    
    # Prints empty space to seperate data printed by function.
    print('\n'*2)

def station_stats(df):
    """Takes a DataFrame and displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    # Marking time as start time in order to calculate the time taken by function to execute.
    start_time = time.time()
    
    # Counts the number of times an unique value appears in the Start Station column and prints the name of Start Station appearing the most       and its count in the column.
    pop_start_station_count = df['Start Station'].value_counts().max()
    pop_start_station = df['Start Station'].mode()[0]
    print('Most popular Start Station :',pop_start_station,'\tcount:',pop_start_station_count)

    # Counts the number of times an unique value appears in the End Station column and prints the name of End Station appearing the most and       its count in the column.
    pop_end_station_count = df['End Station'].value_counts().max()
    pop_end_station = df['End Station'].mode()[0]
    print('Most popular End Station :',pop_end_station,'\tcount:',pop_end_station_count)
    
    # Combines two columns in DataFrame and prints the most frequent value in this column along with its count in column
    df['journey'] = df['Start Station'] + '  TO  ' + df['End Station']
    most_pop_trip = df['journey'].mode()[0]
    max_freq_count = df.groupby(['Start Station','End Station'])['Start Time'].count().max()
    print('The  most popular frequent trip :',most_pop_trip,'\tcount :',max_freq_count)
    
    # Marking the time as end time for calculation of time taken for execution of above code.
    print("\nThis took {} seconds.".format(time.time() - start_time))
    
    # Prints empty space to seperate data printed by function.
    print('\n'*2)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    # Marking time as start time in order to calculate the time taken by function to execute.
    start_time = time.time()

    # Using numpy's sum function to calculate total of trip durations.
    total_time = np.sum(df['Trip Duration'])
    print('Total travel time duration :',total_time)

    # Using numpy's mean function to calculate average trip duration.
    mean_time = np.mean(df['Trip Duration'])
    print('Mean travel time duration :',mean_time)

    # Marking the time as end time for calculation of time taken for execution of above code.
    print("\nThis took {} seconds.".format(time.time() - start_time))
    
    # Prints empty space to seperate data printed by function.
    print('\n'*2)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    # Marking time as start time in order to calculate the time taken by function to execute.
    start_time = time.time()

    # Calculating the number of unique rows in 'User_type' column and printing each type along with their respective count. 
    user_type = df['User Type'].value_counts()
    print('Total SUBSCRIBERS :',user_type['Subscriber'],'\tTotal CUSTOMERS:',user_type['Customer'])
    
    # Conditional statement to check if the city entered by user is 'washington'.If yes,then it displays no data as the columns dont exist          in washingtons csv file.If not,then it displays the result.
    if city == 'washington':
        print('No Gender and Bith year info to display')
    else:
        # Counts number of rows for each unique value in 'Gender' column and prints each type along with its count in this column.
        gender = df['Gender'].value_counts()
        print('Total MALES :',gender['Male'],'\tTotal FEMALES :',gender['Female'])
        
        # prints most frequently occuring value in 'Birth Year' as most common birth year,minimum of those as earliest birth year and                  maximum of those as latest birth year
        latest_birth_year = df['Birth Year'].max()
        earliest_birth_year = df['Birth Year'].replace([0,None]).min(skipna= True)
        common_birth_year = df['Birth Year'].replace([0,None]).mode()[0]
        print('Most common birth year :',common_birth_year,'\nEarliest birth year :',earliest_birth_year,'\nLatest birth year :',latest_birth_year)

    # Marking the time as end time for calculation of time taken for execution of above code.
    print("\nThis took {} seconds.".format(time.time() - start_time))

    # Prints empty space to seperate data printed by function.z
    print('\n'*2)

def raw_data(df,city):
    """ Takes DataFrame and returns row by row data as per input provided by user. """ 
    # Asks user if user want to print individual data and keeps on printing data row by row until user types 'No'.
    response = input('Do you want to see individual data ? ')
    i = 0
    while response.lower() == 'yes' or response.lower() == 'y':
        # creates a dictionary to represent the individual data
        user = {'id' : df.loc[i][0],
                'Start Time' : df['Start Time'][i],
                'End Time' : df['End Time'][i],
                'Trip Duration(sec)' : df['Trip Duration'][i],
                'Start Station' : df['Start Station'][i],
                'End Station' : df['End Station'][i],
                'User Type' : df['User Type'][i]  }
        # Ensures that the code prints all information about every user for each city
        if city != 'washington':
            user['Gender'] = df['Gender'][i]
            user['Birth Year'] = df['Birth Year'][i]
        # prints information for each raw in the frame as a dictionary
        print(user)
        response = input('\nDo you want to print individual data ? Enter yes or no : ')
        i += 1
    return

def main():
    # Asks the user if user wants to explore bikeshare and if the input is 'yes',it executes the code,prints the result and asks again until        user enters 'no'.
    restart = input('\nWould you like to expolre bikeshare data? Enter yes or no.\n')
    while restart.lower() == 'yes' or restart.lower() == 'y': # conditional statement to start execution
        city, month, day = get_filters()    # function is called and returned values are assigned to variables
        df = load_data(city, month, day)     # function is called and returned value is assigned to variable
        time_stats(df,month,day)             # function called with three arguments
        station_stats(df)                    # function called
        trip_duration_stats(df)              # function called
        user_stats(df,city)                  # function called with two argumnets
        raw_data(df,city)                    # function called with two argumnets
        restart = input('\nWould you like to restart? Enter yes or no.\n')
       
if __name__ == '__main__':
    # Check if the code is running as main or as imported.If its main,the main function is called.
    main()