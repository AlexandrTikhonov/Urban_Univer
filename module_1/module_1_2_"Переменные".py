quantity_completed_HW = 12
quantity_spent_hours = 1.5
name_course = "Python"
time_for_1_task = quantity_spent_hours / quantity_completed_HW
print(
    f"Курс: {name_course}, всего задач:{quantity_completed_HW}, затрачено часов:{quantity_spent_hours}, "
    f"среднее время выполнения {time_for_1_task} часа"
)
