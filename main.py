def main():
    print("Hello from na-metday50!")
    
    from app.ui import st, RED, LIGHT_GREY
    from app.config import HIGH_SYSTOLIC, HIGH_DIASTOLIC, LOW_SYSTOLIC, LOW_DIASTOLIC

    st.title("BP Medicine Advisor 💊")
    st.write("Enter your blood pressure value and select the time.")

    systolic = st.number_input("Systolic BP", min_value=50, max_value=250, value=120)
    diastolic = st.number_input("Diastolic BP", min_value=30, max_value=150, value=80)
    time = st.selectbox("Time", ["Morning", "Night"])

    if st.button("Get Advice"):
        advice = ""
        is_high = systolic >= HIGH_SYSTOLIC or diastolic >= HIGH_DIASTOLIC
        is_low = (systolic <= LOW_SYSTOLIC or diastolic <= LOW_DIASTOLIC)
        is_normal = not is_high and not is_low
        critical_low = systolic < 100
        if(critical_low):
            advice = "Inform immediately - Critically low"
        elif time == "Night" and is_high:
            advice = "Night time BP is high: Take metxl."
        elif time == "Morning" and is_high:
            advice = "Morning BP is high: Do not take sodium today."
        elif is_low and time == "Morning":
            advice = "Morning BP is low: Take sodium tablet."
        elif is_low and time == "Night":
            advice = "Night BP is low, Take buttermilk and if BP is low next day take sodium"
        elif is_normal:
            advice = "BP is normal: No further action needed."
        else:
            advice = "BP does not fall in any of the regular conditions - Inform"
        st.success("Advice:")
        st.write(advice)


if __name__ == "__main__":
    main()
