import streamlit as st

# タイトル
st.title("社会情報プロジェクト実習I") # タイトル

# 見出し
st.subheader("基本オブジェクト") # 見出し

# テキスト
st.write("テキストの練習")

# 画像
from PIL import Image 
image = Image.open("画像.png")
st.image(image)

# テキストボックス
studentID = st.text_input("学籍番号") # テキストボックスの入力内容

# セレクトボタン
years = st.selectbox("学年", ("1年", "2年", "3年", "4年")) # 選択肢

# ラジオボックス
class_choice = st.radio("クラス", ("Aクラス","Bクラス")) # 選択肢

# カレンダー
date = st.date_input("出席日")

# スライダー
slider = st.slider("出席回数", 0, 14, 0) # 最小値、最大値、初期値

# チェックボックス
checked = st.checkbox("後期も受講")

# ボタン
btn = st.button("出席")  # ボタンが押されたTrue,押されないとFalse

if btn: # ボタンが押されたときの処理
    st.write(f"{date}|{years}|{class_choice}|{studentID}|出席{slider}回目") # 画面に出力
    if checked: st.write(f"後期も受講!!") # 画面に出力
    print(f"出席:{studentID}") # コンソールに出力