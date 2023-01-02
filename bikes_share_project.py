
import time
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?')
        city = city.lower()
        if city not in CITY_DATA:
            print('please enter a valid city from the available list of cities')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter the data by month, or show all?')
        months = ['all', 'january', 'february','march', 'april', 'may', 'june']
        month = month.lower()
        if month not in months :
            print('please enter a valid month to filter with, or type all')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to filter the data by week day, day, or show all?')
        week_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = day.lower()
        if day not in week_days:
            print('please enter a valid day to filter with, or type all')
        else:
            break
        
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_number = int(df['month'].mode()[0])
    print('The most common month in your assigned time filter is ' + months[month_number-1])

    # display the most common day of week
    print('The most common day of week in your assigned time filter is: ' + df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common start hour in your assigned time filter is: ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: ' + df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most common end station is: ' + df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start + End'] = 'Start: ' + df['Start Station'] + ' _ End: ' +df['End Station']
    print('the most frequent combination of start station and end station trip is :\n' + df['Start + End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() 
    hours = total_travel_time // 3600
    minutes = (total_travel_time % 3600) // 60
    seconds = (total_travel_time % 3600) % 60
    print('Total travel time is : ' + str(hours) + ' hours & ' + str(minutes) + ' minutes & ' + str(seconds) + ' seconds.')
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = mean_travel_time // 60
    mean_seconds = mean_travel_time % 60
    print('Mean travel time is : ' + str(mean_minutes) + ' minutes & ' + str(mean_seconds) + ' seconds.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_users = df['User Type'].value_counts()
    print('here is a cont of different type of users who used bike share : \n' +  str(count_of_users))

    # Display counts of gender
    if 'Gender' in df.columns:
        print('here is a gender analysis of bike share users :\n' + str(df['Gender'].value_counts()))
    else:
        print('the dataset for this city does not contain gender information')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest user year of birth is :\n' + str(df['Birth Year'].min()))
        print('The most recent year of birth is :\n' + str(df['Birth Year'].max()))
        print('The most common year of birth is: \n' + str(df['Birth Year'].mode()[0]))
    else:
        print("the dataset for this city doesn't contain information about birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """asks user whether he need to see original data rows or not,
    and in case he clicks yes 5 rows are previewed then
    asks user again if he needs to see another 5 more rows,
    the function keeps running untill user tyoes no."""
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        view_data = view_data.lower()
        if view_data not in ['yes','no']:
            print('please enter a valid answer either yes or no')
        else:
            break
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
