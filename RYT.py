#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
st.header('*looking to your volting eligiability*')
age=st.number_input('what your age')
if age >=18:
    st.write('you can vote')
else:
    st.write('you can not vote')


# In[ ]:




