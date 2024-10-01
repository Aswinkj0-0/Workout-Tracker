import streamlit as st
import time as t
from  streamlit_card import card


class WorkoutTracker:
    def __init__(self, name, age, level, total_time):
        self.name = name
        self.age = age
        self.level = level
        self.time = total_time

    levels={ 1 : {'sets': 3, 'reps': 12, 'rest': 60},
             2 : {'sets': 4, 'reps': 15, 'rest': 45},
             3 : {'sets': 5, 'reps': 20, 'rest': 30}}

    def PreDefinedWorkout(self):

        predesigned_workouts = {
            1: { # Full-Body Workout
                1: {'workout_name': 'Burpess',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                2: {'workout_name': 'Mountain climbers',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                3: {'workout_name': 'Kettlebell Swings',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                4: {'workout_name': 'Deadlifts',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                5: {'workout_name': 'Squat to Press',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']}
            },
            2: { # Flexibility Workout
                1: {'workout_name': 'Smith Squat',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                2: {'workout_name': 'Pull Ups',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                3: {'workout_name': 'Downward Dog',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                4: {'workout_name': 'Deadlifts',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                5: {'workout_name': 'Squat to Press',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']
                    }
            },
            3: {  # Strength Training
                1: {'workout_name': 'Bicep Curl',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                2: {'workout_name': 'Pully pushdown',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                3: {'workout_name': 'Kettlebell Swings',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                4: {'workout_name': 'Deadlifts',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                5: {'workout_name': 'Squat to Press',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']
                    }
            },
            4 : {  # High-Intensity Interval Training (HIIT)
                1: {'workout_name': 'Burpess',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                2: {'workout_name': 'Mountain climbers',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                3: {'workout_name': 'Kettlebell Swings',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                4: {'workout_name': 'Deadlifts',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                5: {'workout_name': 'Squat to Press',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']
                    }
            },
            5: {  # Cardio Workouts
                1: {'workout_name': 'Squats',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                2: {'workout_name': 'Cycling',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                3: {'workout_name': 'Kettlebell Swings',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                4: {'workout_name': 'Deadlifts',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']},

                5: {'workout_name': 'Squat to Press',
                    'sets': WorkoutTracker.levels[self.level]['sets'],
                    'reps': WorkoutTracker.levels[self.level]['reps'],
                    'rest': WorkoutTracker.levels[self.level]['rest']
                    }
            }
        }
        st.text("Do you want to choose from the pre-designed workouts : \n")

        if st.checkbox('yes'):

            choice = st.selectbox("Enter the category :",['1. Full-Body Workouts' , '2. Flexibility Workouts ','3. Strength Training ', '4. High-Intensity Interval Training (HIIT)' , '5. Cardio Workout'])
            choice = [int(i) for i in choice if i.isnumeric()]

            st.header("These are the Exercises in your choice \n")

            for i in range(1, len(predesigned_workouts[choice[0]])+1):
                st.text('{}'.format(predesigned_workouts[choice[0]][i]['workout_name']))

            self.time_of_set = st.number_input("Enter the time you have for the exercise (in seconds) : ")
            total_time_for_wrkout = 0

            for k in range(1, len(predesigned_workouts[choice[0]])+1):
                total_time_for_wrkout += (predesigned_workouts[choice[0]][k]['sets'] * self.time_of_set + predesigned_workouts[choice[0]][k]['rest']) * len(predesigned_workouts[choice[0]])

            st.text(f"Estimated time of your session : {(total_time_for_wrkout // 60) // 60 } hour and {(total_time_for_wrkout // 60) % 60} minutes")


            st.text("do you want to start timer ?:")
            if st.checkbox('yes,start timer'):

                for i in range(1, len(predesigned_workouts)+1):

                    st.info(predesigned_workouts[choice[0]][i]['workout_name'])
                    # print()
                    st.write('Number of sets : ',predesigned_workouts[choice[0]][i]['sets'])
                    st.write(f'Number of reps : ',predesigned_workouts[choice[0]][i]['reps'])
                    st.write(f'Take ',predesigned_workouts[choice[0]][i]['rest'],'seconds rest in between sets')

                    self.StartTimer()

                st.success("You have completed your workout")

                return True

            if st.checkbox('no, i have a timer'):

                st.success("Feel free to use anytime.....")

                return True


        if st.checkbox ('no, i want a custom workout'):
            self.CustomWorkout()
    def CustomWorkout(self):
        st.header("Custom Workout plan")
        print()
        no_of_execise = st.number_input('Enter the number of execises : ')
        sets = st.number_input("Enter the number of sets : ")
        reps = st.number_input("Enter the number of reps : ")
        time_of_set = st.number_input("Enter the time for each set (in seconds): ")

        rest_time_of_set= WorkoutTracker.levels[self.level]['rest']
        total_time = ( time_of_set * sets + rest_time_of_set ) * no_of_execise
        self.time_of_set = time_of_set
        time_in_minutes = total_time //60


        st.text(f"Estimated time of your session : {time_in_minutes // 60} hours and {time_in_minutes % 60} minutes")
        # Custom_choice = st.text_input('Do you want to Start timer(Y/N) : ')
        st.text('Do you want to Start timer? : ')
        # if Custom_choice.lower() == 'y':
        if st.checkbox('yes, start timer for my workout'):
            self.StartTimer()

        if st.checkbox('no, dont need a timer') :
            st.success("Thank you for choosing the Workout tracker")

    def StartTimer(self):
        timer = st.progress(0)
        # print(self.time_of_set)

        for i in range(100):
            t.sleep((self.time_of_set/100)) # convert the progres bar according to the time
            timer.progress(i+1)
            print('first bar',i)

            if i == 99:
                t.sleep(1)
                st.warning("Start your rest \n")

                for j in range(100):
                    print('second prog_bar',j)
                    t.sleep((WorkoutTracker.levels[self.level]['rest'])/100)
                    timer.progress(j+1)
                t.sleep(1)



st.title('Welcome to workout tracker')

name = st.text_input('Your name :')
age =st.number_input("Your age :")

total_time = st.number_input("Enter your workout time (in hr) : ")
total_time *= 60


level = st.selectbox('Level of fitness',['Beginner','Intermediate','Advanced'])

if level == 'Beginner': level = 1
elif level == 'Intermediate' : level = 2
elif level == 'Advanced' : level = 3


print()
st.text("Available Pre-designed Workouts ")
print()

user1 = WorkoutTracker(name, age, level, total_time)
user1.PreDefinedWorkout()



