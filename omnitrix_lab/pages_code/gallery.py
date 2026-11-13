"""
gallery.py — Gallery page.
Upload images, display in a grid, and apply simple Pillow filters.
"""

import streamlit as st
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import io
from utils.helpers import render_section_title


def show():
    """Render the Gallery page."""
    render_section_title("🖼️ GALLERY")

    st.markdown(
        '<p style="color:#a0a0a0;">Upload images and apply Omnitrix-themed filters.</p>',
        unsafe_allow_html=True,
    )

    # Initialize session state for gallery images and edited image
    if "gallery_images" not in st.session_state:
        st.session_state.gallery_images = []
    if "edited_image_data" not in st.session_state:
        st.session_state.edited_image_data = None

    # --- Upload ---
    uploaded_files = st.file_uploader(
        "Upload images (PNG / JPG)",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="gallery_upload",
    )

    # Store uploaded images in session state
    if uploaded_files:
        st.session_state.gallery_images = []
        for uf in uploaded_files:
            img = Image.open(uf).convert("RGB")
            st.session_state.gallery_images.append({
                "name": uf.name,
                "image": img,
            })

    images = st.session_state.gallery_images

    if not images:
        st.info("📷 Upload some images to see them here.")
        return

    # --- Gallery Grid ---
    render_section_title("📸 YOUR IMAGES")
    cols = st.columns(min(len(images), 3))
    for idx, img_data in enumerate(images):
        with cols[idx % 3]:
            st.image(img_data["image"], caption=img_data["name"], use_container_width=True)

    # --- Editor ---
    st.markdown("---")
    render_section_title("🎨 IMAGE EDITOR")

    # Pick which image to edit
    names = [img["name"] for img in images]
    selected_name = st.selectbox("Select an image to edit:", names, key="gallery_select")
    selected_idx = names.index(selected_name)
    original = images[selected_idx]["image"]

    # Editor controls
    e1, e2, e3, e4 = st.columns(4)

    with e1:
        new_width = st.number_input("Width (px)", min_value=16, max_value=4096, value=original.width, key="gallery_w")
    with e2:
        new_height = st.number_input("Height (px)", min_value=16, max_value=4096, value=original.height, key="gallery_h")
    with e3:
        rotation = st.slider("Rotate (°)", 0, 360, 0, step=15, key="gallery_rot")
    with e4:
        filter_choice = st.selectbox(
            "Filter",
            ["None", "Grayscale", "Omnitrix Green Tint", "Blur", "Sharpen", "Edge Detect"],
            key="gallery_filter",
        )

    if st.button("⚡ Apply Edits", key="gallery_apply"):
        edited = original.copy()

        # Resize
        if new_width != original.width or new_height != original.height:
            edited = edited.resize((new_width, new_height), Image.LANCZOS)

        # Rotate
        if rotation:
            edited = edited.rotate(rotation, expand=True, fillcolor=(10, 15, 10))

        # Filters
        if filter_choice == "Grayscale":
            edited = ImageOps.grayscale(edited).convert("RGB")
        elif filter_choice == "Omnitrix Green Tint":
            # Apply a green tint overlay
            edited = _apply_green_tint(edited)
        elif filter_choice == "Blur":
            edited = edited.filter(ImageFilter.GaussianBlur(radius=3))
        elif filter_choice == "Sharpen":
            edited = edited.filter(ImageFilter.SHARPEN)
        elif filter_choice == "Edge Detect":
            edited = edited.filter(ImageFilter.FIND_EDGES)

        # Store in session state
        buf = io.BytesIO()
        edited.save(buf, format="PNG")
        st.session_state.edited_image_data = {
            "image": edited,
            "bytes": buf.getvalue(),
            "name": f"omnitrix_{selected_name}",
        }

    # Display edited image if available
    if st.session_state.edited_image_data is not None:
        st.image(
            st.session_state.edited_image_data["image"],
            caption=f"Result: {st.session_state.edited_image_data['name']}",
            use_container_width=True,
        )

        st.download_button(
            label="⬇️ Download Edited Image",
            data=st.session_state.edited_image_data["bytes"],
            file_name=st.session_state.edited_image_data["name"],
            mime="image/png",
            key="gallery_download",
        )


def _apply_green_tint(img):
    """Apply a neon green Omnitrix tint to an image."""
    # Increase green channel, reduce red and blue
    r, g, b = img.split()
    # Enhance green
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0.6)  # Reduce saturation a bit
    r, g, b = img.split()
    # Boost green, dim red and blue
    r = r.point(lambda x: int(x * 0.5))
    g = g.point(lambda x: min(255, int(x * 1.4 + 30)))
    b = b.point(lambda x: int(x * 0.4))
    return Image.merge("RGB", (r, g, b))
