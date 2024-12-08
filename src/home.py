from src.pos_tag import pos_tagger, stanford_formatter, list_pos_tag

from annotated_text import annotated_text
import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Balinese POS Tagging")
st.write("ᬒᬁᬲ᭄ᬯᬲ᭄ᬢ᭄ᬬᬲ᭄ᬢᬸ᭟")

st.markdown(
    """
        Balinese POS Tagging is a simple and fun tool to learn about the parts of speech in the Balinese language. 
        By entering a sentence in Balinese, you can instantly see how each word is categorized—whether it's a noun, verb, adjective, or other part of speech. 
        It's an easy way to improve grammar and understand sentence structure in Balinese.
    """
)
st.divider()


col_origin, col_translate = st.columns(2)

with col_origin:
    txt = st.text_area(
        "Text", value=None, height=200, placeholder="Try: tiang meli baju di peken"
    )

with col_translate:
    if not txt:
        st.write("List of Tagset")
        st.dataframe(
            list_pos_tag(),
            hide_index=True,
            use_container_width=True,
        )
    result = pos_tagger(txt)
    if result:
        st.write("Result")
        annotated_text(result)
        with st.container():
            st.write("Stanford Format")
            st.code(stanford_formatter(result), language=None)
