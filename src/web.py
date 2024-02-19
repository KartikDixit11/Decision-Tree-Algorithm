import streamlit as st
import pickle as pkl


class Web:
    def __init__(self):
        st.title('Iris Flower Prediction')
        self.sl=st.text_input('Sepal Lenght in cm')
        self.sw=st.text_input('Sepal Width in cm')
        self.pl=st.text_input('Petal Length in cm')
        self.pw=st.text_input('Petal Width in cm')
        self.bt=st.button("Submit")
        self.model=pkl.load(open("../artifacts/model.pkl","rb"))
    
    def predict(self):
            try:
                prediction=self.model.predict([[float(self.sl),float(self.sw),float(self.pl),float(self.pw)]])
                st.write('<h3>Prediction</h3>',unsafe_allow_html=True)
                if(prediction==0):
                    st.write('<h4>Your Flower is Iris-Setosa</h4>',unsafe_allow_html=True)
                    st.image("iris setosa.jpg")

                elif(prediction==1):
                    st.write('<h4>Your Flower is Iris-Virginica</h4>',unsafe_allow_html=True)
                    st.image("iris_virginica_virginica_lg.jpg")
                
                elif(prediction==2):
                    st.write('<h4>Your Flower is Iris-Versicolor</h4>',unsafe_allow_html=True)
                    st.image("iris versicolor.jpg")
            except:
                 st.write('Unknow error ouccured')
                 
                

obj=Web()
if obj.bt:
     obj.predict()