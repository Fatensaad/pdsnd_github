import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nwhich city would you like to display? New York City, Chicago or Washington?\n").title()
      if city not in ('New York city', 'Chicago', 'Washington'):
        print("you provided wrong input .. try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month would you like to filter by? (January-June) type 'all' if you don't want to apply filter?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("you provided wrong input .. try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day would you like to filter by ?( Sunday - Saturday ) or type 'all' if you don't want to apply filter?\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("you provided wrong input .. try again.")
        continue
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
    # load into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)



    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_stat = df['Start Station'].mode()[0]
    print('most commonly used start station:', common_start_stat)


    # TO DO: display most commonly used end station

    common_end_stat = df['End Station'].mode()[0]
    print('most commonly used start station:', common_end_stat)


    # TO DO: display most frequent combination of start station and end station trip

    frequent_combination = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip:', common_start_stat, " & ", common_end_stat)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time :', Mean_Travel_Time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('User Types:', User_Types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo Gender type not applicable.")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('\nEarliest Year:', earliest_year)
    except KeyError:
      print("\nEarliest Year: data not applicable.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', most_recent_year)
    except KeyError:
      print("\nMost Recent Year: data not applicable.")

    try:
      most_common_year = df['Birth Year'].mode()[0]
      print('\nMost Common Year:', most_common_year)
    except KeyError:
      print("\nMost Common Year: data not applicable.")

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
        
        print(('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n'))
        view_data = input()
        view_data = view_data.lower()

        start_loc = 5
        while view_data == 'yes':
            print(df[:start_loc])
            print("Do you wish to continue?: ")
            start_loc *= 2
            view_data = input()
            view_data = view_data.lower()


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break 


if __name__ == "__main__":
	main()