import os
import requests

def ask_ai():
    # استدعاء المفتاح أو طلبه بأمان
    api_key = os.getenv("XKIRO_API_KEY", "sk-xt-9bcf17346851572cf190c7055016d366d9374278d9a9bcd7")
    base_url = "https://api.xkiro.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print("=== أداة الاستعلام الذكية عبر الـ API ===")
    user_query = input("أدخل سؤالك للذكاء الاصطناعي (أو اكتب exit للخروج): ")
    
    if user_query.lower() == 'exit':
        return

    payload = {
        "model": "openai/gpt-5.6-sol",
        "messages": [{"role": "user", "content": user_query}]
    }

    try:
        print("\nجاري إرسال الطلب...")
        response = requests.post(base_url, headers=headers, json=payload)
        result = response.json()
        
        print("\n--- الإجابة ---")
        print(result['choices'][0]['message']['content'])
    except Exception as e:
        print(f"\nحدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    ask_ai()