import streamlit as st
import requests
import json
st.title("ETCD Project")

# Check etcd connection
getConn = requests.get("http://backend:8000/getConnStatus")
if getConn.content == 0:
    st.err("Unable to connect to ETCD")

else:
    with st.expander("Get All Keys"):
        getKeys = requests.get("http://backend:8000/listKeys")
        for x in json.loads(getKeys.content.decode('utf-8') ):
            st.text(x)
    with st.expander("Get Value for Key"):
        getKey = st.text_input("Enter the Key",key="1")
        if st.button("Get"):
            getRes = requests.get("http://backend:8000/getVal?key="+getKey.replace(" ","+"))
            st.text(getRes.content.decode('utf-8'))
    with st.expander("Put Key-Value Pair"):
        key = st.text_input("Enter the Key",key="2")
        val = st.text_input("Enter the Value")
        if st.button("Put"):
            putdict = {"key":key,"val":val}
            print(putdict)
            res = requests.post("http://backend:8000/putKeyVal",json=putdict)
            st.text(res.content)
    with st.expander("Delete Key-Value Pair"):
         delKey = st.text_input("Enter the Key",key="3")
         if st.button("Delete"):
            getKey = requests.get("http://backend:8000/deleteVal?key="+delKey.replace(" ","+"))
            st.text(getRes.content)