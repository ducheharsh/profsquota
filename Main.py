import calendar
def Calulate_attendance(total_lectures, attended_lectures):
  results = (total_lectures * 0.75) - attended_lectures
  return max(0, results)

def Days(month, year):
  obj = calendar.Calendar()
  original_list = []

  for day in obj.itermonthdays2(year, month):
      original_list.append(day)

  filtered_list = []
  for ele in original_list:
     if ele[0] != 0:
        filtered_list.append(ele)

  no_mon = []
  no_tue = []
  no_wed = []
  no_thu = []
  no_fri = []
  no_sat = []
  day_dict = {'mon':0 ,'tue':0 ,'wed':0 , 'thu':0 , 'fri':0 , 'sat':0 }

  for num in filtered_list:
    if num[1] == 0:
        no_mon.append(num)
        day_dict['mon'] = len(no_mon)
        
  for num in filtered_list:
    if num[1] == 1:
        no_tue.append(num)
        day_dict['tue'] = len(no_tue)
       
  for num in filtered_list:
    if num[1] == 2:
        no_wed.append(num)
        day_dict['wed'] = len(no_wed)
   
  for num in filtered_list:
    if num[1] == 3:
        no_thu.append(num)
        day_dict['thu'] = len(no_thu)
   
  for num in filtered_list:
    if num[1] == 4:
        no_fri.append(num)
        day_dict['fri'] = len(no_fri)

  for num in filtered_list:
    if num[1] == 5:
        no_sat.append(num)
        day_dict['sat'] = len(no_sat)

  return day_dict

def weekends(month, year):
  obj = calendar.Calendar()
  original_list = []

  for day in obj.itermonthdays2(year, month):
      original_list.append(day)

  filtered_list = []
  for ele in original_list:
     if ele[0] != 0:
        filtered_list.append(ele)
  no_sat = []

  for num in filtered_list:
    if num[1] == 5:
        no_sat.append(num)
  
  if len(no_sat) >= 3:
     return 2
  else: 
     return 1

def holidays(month, year):
   if month == 8:
      return 2
   if month == 9:
      return 2
   if month == 10:
      return 2
   if month == 11:
      return 4
   if month == 12:
      return 1

def total_holidays(month, year):
   return int(weekends(month,year) + holidays(month, year))

def main():
   print("----------------------------------------------------------------")
   month = int(input("Enter month (1-12): "))
   year = int(input("Enter year: "))
   print("----------------------------------------------------------------")
   No_of_subjects= int(input("No. of subjects: "))
   subjects = []
   day_dict = Days(month, year)
   holiday = holidays(month, year)
   sat_reduction = int(weekends(month, year))
   
   for i in range(No_of_subjects):
     subjects.append(input("Name of the subject: "))
     print("----------------------------------------------------------------")
     lec_on_mon = int(input("Total number of lectures of " + subjects[i] + " on Monday \n(Enter 0 if none): "))
     lec_on_tue = int(input("Total number of lectures of " + subjects[i] + " on Tuesday \n(Enter 0 if none): "))
     lec_on_wed = int(input("Total number of lectures of " + subjects[i] + " on Wednesday \n(Enter 0 if none): "))
     lec_on_thu = int(input("Total number of lectures of " + subjects[i] + " on Thursday \n(Enter 0 if none): "))
     lec_on_fri = int(input("Total number of lectures of " + subjects[i] + " on Friday \n(Enter 0 if none): "))
     lec_on_sat = int(input("Total number of lectures of " + subjects[i] + " on Saturday \n(Enter 0 if none): "))
     total_lectures = (((lec_on_mon * day_dict["mon"]) + (lec_on_tue * day_dict["tue"]) 
     + (lec_on_wed * day_dict["wed"])
     + (lec_on_thu * day_dict["thu"]) + (lec_on_fri * day_dict["fri"]) 
     + ((lec_on_sat * day_dict["sat"]) - sat_reduction ) ) - holiday)
     print("----------------------------------------------------------------")
     attended_lectures = int(input("No. of lectures you attended: "))
     print("Total number of lectures of ", subjects[i], " (excluding holidays) are: " , total_lectures )
     print("No. of lectures you need to attend of ", subjects[i], " are " , int(Calulate_attendance(total_lectures, attended_lectures)))

main()
