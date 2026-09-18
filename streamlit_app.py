import streamlit as st

st.set_page_config(page_title="Судебная практика", page_icon="⚖️", layout="centered")

STATIC_PATH = "app/static/practice.html"

st.title("⚖️ Судебная практика")
st.write(
    "Инструмент опубликован как статический файл этого Streamlit-приложения. "
    "Нажмите кнопку ниже, чтобы открыть его — ссылка работает с любого устройства."
)

st.link_button("Открыть инструмент поиска по судебной практике →", STATIC_PATH, use_container_width=True)

st.caption(
    "Если кнопка не открывает страницу напрямую, скопируйте адрес текущего приложения "
    "и допишите к нему `/app/static/practice.html`."
)

st.divider()
st.caption("Прямая встроенная версия ниже (может грузиться дольше из-за размера файла):")

st.markdown(
    f'<iframe src="{STATIC_PATH}" width="100%" height="900" style="border:1px solid #ddd;border-radius:8px;"></iframe>',
    unsafe_allow_html=True,
)
