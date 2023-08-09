import solara
import pickle
from PIL import Image
tfidf = pickle.load(open(r"C:\Users\KALYAN\Desktop\Projects\Spam E-Mail Classification\Pickle Files\feature.pkl", "rb"))
model = pickle.load(open(r"C:\Users\KALYAN\Desktop\Projects\Spam E-Mail Classification\Pickle Files\model.pkl", "rb"))

app = solara.app(title="Spam E-Mail Classification")
@app.page("Spam E-Mail Classifier")
def spam_email_classifier():
    input_mail = solara.text_input("Enter the Message")

    if solara.button("Predict"):
        vector_input = tfidf.transform([input_mail])
        result = model.predict(vector_input)
        solara.success(f"This is a {'Spam Mail' if result == 0 else 'Ham Mail'}")

@app.page("Home")
def home():
    image = Image.open("images.jpg")
    solara.image(image)

# Set the home page as the default page
app.set_default_page("Home")
if __name__ == "__main__":
    app.run()
