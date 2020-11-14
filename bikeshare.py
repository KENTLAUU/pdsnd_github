<<<<<<< HEAD
<<<<<<< HEAD

||||||| d2cb8b1
=======
 #
 DOCSTRING
 #

# Linecomment

>>>>>>> f3139c96c8326781334dde3786b7eee67a4193ce
||||||| ecd9c69
=======
 #
refactor: cleaned up extra spaces between code and notes
 #

>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')

    while True:
        city = input('Which of these cities do you want to explore : chicago, new york city or washington? \n> ').strip().lower() #was lower()
        if city in cities:
<<<<<<< HEAD
            break
    # get user input for month (all, january, february, ... , june)
||||||| ecd9c69
            break         
    # get user input for month (all, january, february, ... , june)
=======
            break
# get user input for month (all, january, february, ... , june)
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
    while True:
        month = input('Now you have to enter a month to get some months result \n> {} \n> '.format(months))
        if month in months:
            break
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Now you have to enter a dau to get some days result \n> {} \n> '.format(days))
        if day in days:
            break
<<<<<<< HEAD

||||||| ecd9c69
 
=======
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06

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

# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

# filter by month if applicable
    if month != 'all':
<<<<<<< HEAD
        # use the index of the months list to get the corresponding int

||||||| ecd9c69
        # use the index of the months list to get the corresponding int
       
=======
    # use the index of the months list to get the corresponding int
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
        month = months.index(month)

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

# filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', months[common_month].title())

# TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of week:', common_day)

# TO DO: display the most common start hour
# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
<<<<<<< HEAD

||||||| ecd9c69
    
=======
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
    print('Most Common Start Station:', common_start_station)

# TO DO: display most commonly used end station
    common_end_station  = df['End Station'].mode()[0]
<<<<<<< HEAD

||||||| ecd9c69
    
=======
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
    print('Most Common End Station:', common_end_station)


# TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + df['End Station']).mode()[0]
<<<<<<< HEAD

||||||| ecd9c69
    
=======
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
    print('Most frequent combination of start station and end station trip:', common_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', total_travel)

# TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

# TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:',user_types)

<<<<<<< HEAD
    # TO DO: Display counts of gender
||||||| ecd9c69
    # TO DO: Display counts of gender  
=======
# TO DO: Display counts of gender
>>>>>>> 8061123b482ca680003820d02d3d58cb0317fd06
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('No gender information in this city.')

# Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print('Earliest year of birth:',earliest)
        recent = df['Birth_Year'].max()
        print('Most recent ear of birth:', recent)
        common_birth = df['Birth Year'].mode()[0]
        print('Most common ear of birth:', common_birth)
    else:
        print("No birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
