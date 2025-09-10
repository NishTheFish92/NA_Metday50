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
            advice = "### Inform immediately. Take sodium. Priority is to get BP back up. BP is Critically low"
        elif is_normal:
            advice = "### BP is normal: Take sodium every alternate day and take Telday40 like usual."
        elif time == "Night" and is_high:
            advice = "### Night time BP is high: Take MetXL and Telday40. (MetXL should be taken if and only if this message is seen)"
        elif time == "Morning" and is_high:
            advice = "### Morning BP is high: Sodium tablet is to be taken every alternate day. However, as BP is high do not take sodium tablet today. Take Telday40 like usual."
        elif is_low and time == "Morning":
            advice = "### Morning BP is low: Sodium tablet is to be taken every alternate day. However, as BP is low take sodium tablet today. Take Telday40 like usual."
        elif is_low and time == "Night":
            advice = "### Night BP is low, Take buttermilk. Take Telday40 even if BP is low."
        else:
            advice = "### BP does not fall in any of the regular conditions - Inform or call immediately so that further action can be determined."
        st.success("Advice:")
        st.write(advice)


if __name__ == "__main__":
    main()
