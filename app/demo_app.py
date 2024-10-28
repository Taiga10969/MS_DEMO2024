import streamlit as st

st.set_page_config(
    page_title="MS_DEMO",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.text("藤吉グループ DEMO")
st.title("仮説文と結論文の真偽判定と判定根拠の可視化")

# 入力欄の設定
hypo_text = st.text_input("**仮説文**", autocomplete="off")
conc_text = st.text_input("**結論文**", autocomplete="off")


method = st.radio(
    "**判定根拠の可視化手法を選択**",
    ["Attention", "Gradient", "Input occlusion", "SHAP"]
)


if hypo_text and conc_text:
    # 各処理手法に対応するボタンを配置
    if st.button("処理"):
        st.divider()

        if method == "Attention":

            # 処理
            score = 0
            html_data = """<span style="background-color: rgb(255, 240, 240);">The</span> <span style="background-color: rgb(255, 243, 243);">photocatalytic</span> <span style="background-color: rgb(255, 229, 229);">performance</span> <span style="background-color: rgb(255, 247, 247);">of</span> <span style="background-color: rgb(255, 246, 246);">Cs4PbBr6/WS2</span> <span style="background-color: rgb(255, 239, 239);">nanocomposites</span> <span style="background-color: rgb(255, 253, 253);">is</span> <span style="background-color: rgb(255, 251, 251);">expected</span> <span style="background-color: rgb(255, 255, 255);">to</span> <span style="background-color: rgb(255, 252, 252);">be</span> <span style="background-color: rgb(255, 0, 0);">superior</span> <span style="background-color: rgb(255, 243, 243);">to</span> <span style="background-color: rgb(255, 249, 249);">that</span> <span style="background-color: rgb(255, 253, 253);">of</span> <span style="background-color: rgb(255, 230, 230);">pristine</span> <span style="background-color: rgb(255, 216, 216);">Cs4PbBr6</span> <span style="background-color: rgb(255, 249, 249);">nanocrystals</span> <span style="background-color: rgb(255, 255, 255);">for</span> <span style="background-color: rgb(255, 247, 247);">the</span> <span style="background-color: rgb(255, 236, 236);">degradation</span> <span style="background-color: rgb(255, 253, 253);">of</span> <span style="background-color: rgb(255, 247, 247);">organic</span> <span style="background-color: rgb(255, 229, 229);">dyes</span> <span style="background-color: rgb(255, 254, 254);">under</span> <span style="background-color: rgb(255, 233, 233);">visible</span> <span style="background-color: rgb(255, 250, 250);">light</span> <span style="background-color: rgb(255, 246, 246);">illumination.</span> <br><br><span style="background-color: rgb(255, 222, 222);">The</span> <span style="background-color: rgb(255, 252, 252);">research</span> <span style="background-color: rgb(255, 251, 251);">conclusion</span> <span style="background-color: rgb(255, 255, 255);">can</span> <span style="background-color: rgb(255, 249, 249);">be</span> <span style="background-color: rgb(255, 245, 245);">extracted</span> <span style="background-color: rgb(255, 251, 251);">from</span> <span style="background-color: rgb(255, 251, 251);">the</span> <span style="background-color: rgb(255, 250, 250);">conclusion</span> <span style="background-color: rgb(255, 255, 255);">section</span> <span style="background-color: rgb(255, 243, 243);">as:</span> <span style="background-color: rgb(255, 252, 252);">"The</span> <span style="background-color: rgb(255, 241, 241);">Cs4PbBr6/WS2</span> <span style="background-color: rgb(255, 240, 240);">nanocomposites</span> <span style="background-color: rgb(255, 244, 244);">exhibit</span> <span style="background-color: rgb(255, 233, 233);">superior</span> <span style="background-color: rgb(255, 253, 253);">photocatalytic</span> <span style="background-color: rgb(255, 250, 250);">activity</span> <span style="background-color: rgb(255, 252, 252);">towards</span> <span style="background-color: rgb(255, 248, 248);">the</span> <span style="background-color: rgb(255, 249, 249);">degradation</span> <span style="background-color: rgb(255, 247, 247);">of</span> <span style="background-color: rgb(255, 240, 240);">organic</span> <span style="background-color: rgb(255, 250, 250);">dye,</span> <span style="background-color: rgb(255, 253, 253);">which</span> <span style="background-color: rgb(255, 250, 250);">is</span> <span style="background-color: rgb(255, 247, 247);">attributed</span> <span style="background-color: rgb(255, 248, 248);">to</span> <span style="background-color: rgb(255, 249, 249);">the</span> <span style="background-color: rgb(255, 248, 248);">reduced</span> <span style="background-color: rgb(255, 252, 252);">carrier</span> <span style="background-color: rgb(255, 254, 254);">recombination</span> <span style="background-color: rgb(255, 250, 250);">and</span> <span style="background-color: rgb(255, 249, 249);">increased</span> <span style="background-color: rgb(255, 250, 250);">active</span> <span style="background-color: rgb(255, 252, 252);">radicals</span> <span style="background-color: rgb(255, 251, 251);">formation</span> <span style="background-color: rgb(255, 255, 255);">due</span> <span style="background-color: rgb(255, 250, 250);">to</span> <span style="background-color: rgb(255, 248, 248);">the</span> <span style="background-color: rgb(255, 245, 245);">charge</span> <span style="background-color: rgb(255, 252, 252);">transfer</span> <span style="background-color: rgb(255, 248, 248);">between</span> <span style="background-color: rgb(255, 244, 244);">Cs4PbBr6</span> <span style="background-color: rgb(255, 248, 248);">and</span> <span style="background-color: rgb(255, 239, 239);">WS2."</span>"""

        elif method == "Gradient":
            pass

        elif method == "Input occlusion":
            pass

        elif method == "SHAP":
            pass

        st.text(f"類似度スコア：{score}")
        st.text("判定根拠の可視化結果")
        st.markdown(f"""<div style=font-size:20px; font-weight:bold;'>{html_data}</div>""", unsafe_allow_html=True)