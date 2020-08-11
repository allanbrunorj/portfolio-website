# from joblib import load
# from sklearn.preprocessing import LabelEncoder
# encoder = load("label_encoder.pkl")
import ctypes
print (ctypes.sizeof(ctypes.c_voidp))
def encode_property(property):
       try:
              encoded_property_array = encoder.transform([property])
              return encoded_property_array[0]
       except:
              print('ERRO: MODEL.PY - ENCODE_PROPERTY')


def property_type_dict_encoder():
       mapping = dict(zip(encoder.classes_, range(len(encoder.classes_))))
       print(mapping)