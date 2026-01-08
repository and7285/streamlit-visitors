# ---- Feature Cards Section ----
st.markdown("""
<style>
.features {
    margin-top: 72px;
    padding: 0 24px;
}

.feature-card {
    background-color: #FFFFFF;
    padding: 36px 32px;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    height: 100%;
}

.feature-card h3 {
    font-size: 20px;
    margin-bottom: 12px;
}

.feature-card p {
    font-size: 15px;
    line-height: 1.6;
    color: #555555;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="features">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️ Deepfake Detection</h3>
        <p>
            Detect manipulated media with industry-leading accuracy.
            Our AI identifies even the most subtle synthetic artifacts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Media Integrity Analysis</h3>
        <p>
            Analyze media artifacts inside and out to verify authenticity
            across images, video, and audio.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Instant Verification</h3>
        <p>
            Make high-impact security decisions in seconds with automated,
            real-time verification pipelines.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
