# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    تحويل درجة الحرارة من فهرنهايت إلى سيليزيوس.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    تحويل درجة الحرارة من سيليزيوس إلى فهرنهايت.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # طلب الإدخال من المستخدم
    temp_input = input("أدخل درجة الحرارة للتحويل: ")
    
    # تحقق من أن الإدخال يمكن تحويله إلى رقم
    if temp_input.replace('.', '', 1).isdigit() or (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
        temp = float(temp_input)
    else:
        print("خطأ: الرجاء إدخال قيمة رقمية لدرجة الحرارة.")
        return

    # طلب الوحدة من المستخدم
    unit = input("هل درجة الحرارة التي أدخلتها بوحدة سيليزيوس أم فهرنهايت؟ (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C هي {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F هي {converted_temp}°C")
    else:
        print("وحدة غير صحيحة. الرجاء إدخال 'C' للسيليزيوس أو 'F' للفهرنهايت.")

if __name__ == "__main__":
    main()
