import flet as ft
import random
import plotly.graph_objects as go
from typing import Dict
import base64

LANGS = {
    "golang": {"icon": "🐹", "name": "Go", "exts": ["go", "txt"]},
    "java":   {"icon": "☕", "name": "Java", "exts": ["java", "txt"]},
    "csharp": {"icon": "🔷", "name": "C#", "exts": ["cs", "txt"]},
    "python": {"icon": "🐍", "name": "Python", "exts": ["py", "txt"]},
    "c":      {"icon": "⚡", "name": "C", "exts": ["c", "txt"]},
}

def generate_metrics_for(language_key: str) -> Dict:
    base = {
        "golang": {"ops": 120, "rec": 2, "cycl": 8, "alg": "O(n)", "score": 88},
        "java":   {"ops": 150, "rec": 3, "cycl": 12, "alg": "O(n log n)", "score": 75},
        "csharp": {"ops": 140, "rec": 2, "cycl": 10, "alg": "O(n)", "score": 80},
        "python": {"ops": 180, "rec": 4, "cycl": 15, "alg": "O(n²)", "score": 65},
        "c":      {"ops": 100, "rec": 1, "cycl": 6, "alg": "O(n)", "score": 92},
    }[language_key]

    return {
        "operations": base["ops"] + random.randint(-20, 20),
        "recursion": max(0, base["rec"] + random.randint(-1, 1)),
        "cyclomatic": max(1, base["cycl"] + random.randint(-3, 3)),
        "algorithmic": base["alg"],
        "score": max(0, min(100, base["score"] + random.randint(-10, 10)))
    }

def main(page: ft.Page):
    page.title = "Calculadora de Amigabilidad Ambiental"
    page.window_width = 1100
    page.window_height = 800
    page.padding = 20
    page.theme_mode = "light"

    uploaded_files: Dict[str, dict] = {}
    analysis_results: Dict[str, dict] = {}

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    header = ft.Container(
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=20,
        border_radius=10,
        content=ft.Column([
            ft.Text("🌱 Calculadora de Amigabilidad Ambiental", size=24, weight="w300", color="white"),
            ft.Text("Analiza el impacto ambiental de tus algoritmos en diferentes lenguajes", size=14, color="white54")
        ])
    )

    lang_cards = []
    file_labels = {}

    for key, v in LANGS.items():
        lbl = ft.Text("", size=12)
        file_labels[key] = lbl

        def make_pick_handler(lang_key):
            async def handler(e):
                allowed = LANGS[lang_key]["exts"]
                result = await file_picker.pick_files(allow_multiple=False, allowed_extensions=allowed)
                if not result or not result.files:
                    return
                f = result.files[0]
                name = getattr(f, "name", "unknown")
                content = None
                path = getattr(f, "path", None)
                try:
                    if path:
                        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                            content = fh.read()
                    else:
                        bytes_attr = getattr(f, "bytes", None)
                        if bytes_attr:
                            try:
                                content = bytes_attr.decode("utf-8", errors="ignore")
                            except Exception:
                                content = bytes_attr.decode("latin1", errors="ignore")
                except Exception as ex:
                    content = f"/* ERROR leyendo archivo: {ex} */"

                uploaded_files[lang_key] = {"name": name, "content": content}
                file_labels[lang_key].value = f"📄 {name}"
                update_calculate_button()
                page.update()
            return handler

        card = ft.Container(
            padding=12,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=12,
            content=ft.Column([
                ft.Text(v["icon"], size=28),
                ft.Text(v["name"], weight="w600"),
                ft.Row([
                    ft.ElevatedButton("Seleccionar archivo", on_click=make_pick_handler(key)),
                    ft.Container(width=8)
                ]),
                lbl
            ], horizontal_alignment="center"),
            width=200,
            height=150
        )
        lang_cards.append(card)

    cards_wrap = ft.ResponsiveRow(
        controls=[ft.Container(content=card, col={"xs": 12, "sm": 6, "md": 4, "lg": 3}) for card in lang_cards]
    )

    calculate_btn = ft.ElevatedButton("Calcular Amigabilidad Ambiental", disabled=True)
    results_column = ft.Column([], visible=False, spacing=12, expand=True)

    overall_score_text = ft.Text("0", size=40, weight="w700", color=ft.Colors.GREEN)
    best_lang_text = ft.Text("", size=20, weight="w600")

    table_rows = ft.DataTable(columns=[
        ft.DataColumn(ft.Text("Lenguaje")),
        ft.DataColumn(ft.Text("Operaciones Elementales")),
        ft.DataColumn(ft.Text("Recursión")),
        ft.DataColumn(ft.Text("Complejidad Ciclomática")),
        ft.DataColumn(ft.Text("Complejidad Algorítmica")),
        ft.DataColumn(ft.Text("Puntuación")),
    ], rows=[])

    # ✅ Ahora las gráficas son imágenes base64
    bar_chart = ft.Image(width=500, height=400)
    radar_chart = ft.Image(width=500, height=400)

    def update_calculate_button():
        calculate_btn.disabled = len(uploaded_files) == 0

    def get_score_class(score: int):
        if score >= 80:
            return ft.Colors.GREEN
        if score >= 60:
            return ft.Colors.AMBER_600
        return ft.Colors.RED_600

    def fill_metrics_table():
        table_rows.rows.clear()
        for lang_key, metrics in analysis_results.items():
            ln = LANGS[lang_key]["name"]
            table_rows.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(ln, weight="w600")),
                    ft.DataCell(ft.Text(str(metrics["operations"]))),
                    ft.DataCell(ft.Text(str(metrics["recursion"]))),
                    ft.DataCell(ft.Text(str(metrics["cyclomatic"]))),
                    ft.DataCell(ft.Text(metrics["algorithmic"])),
                    ft.DataCell(ft.Text(str(metrics["score"]), color=get_score_class(metrics["score"]), weight="w700"))
                ])
            )

    def fig_to_base64(fig) -> str:
        """Convierte figura de Plotly en imagen PNG codificada en base64"""
        png_bytes = fig.to_image(format="png")  # requiere kaleido
        return base64.b64encode(png_bytes).decode("utf-8")

    def create_charts():
        # Bar chart
        labels = [LANGS[k]["name"] for k in analysis_results.keys()]
        scores = [analysis_results[k]["score"] for k in analysis_results.keys()]
        Colors = ["#28a745", "#ffc107", "#17a2b8", "#6f42c1", "#fd7e14"][:len(labels)]

        bar_fig = go.Figure(
            data=[go.Bar(x=labels, y=scores, marker_color=Colors)],
            layout=go.Layout(yaxis=dict(range=[0,100]))
        )
        bar_fig.update_layout(title="Comparación por Lenguaje", margin=dict(t=30,l=10,r=10,b=10))
        bar_chart.src_base64 = fig_to_base64(bar_fig)

        # Radar chart
        avg_ops = round(sum([m["operations"] for m in analysis_results.values()]) / len(analysis_results))
        avg_rec = round(sum([m["recursion"] for m in analysis_results.values()]) / len(analysis_results))
        avg_cycl = round(sum([m["cyclomatic"] for m in analysis_results.values()]) / len(analysis_results))

        radar_fig = go.Figure()
        radar_fig.add_trace(go.Scatterpolar(
            r=[avg_ops / 2, avg_rec * 10, avg_cycl * 5],
            theta=['Operaciones Elementales', 'Recursión', 'Complejidad'],
            fill='toself',
            name='Métricas Promedio'
        ))
        radar_fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False, title="Métricas Promedio")
        radar_chart.src_base64 = fig_to_base64(radar_fig)

    async def on_calculate(e):
        analysis_results.clear()
        for lang_key in uploaded_files.keys():
            analysis_results[lang_key] = generate_metrics_for(lang_key)

        scores = [m["score"] for m in analysis_results.values()]
        avg_score = round(sum(scores) / len(scores))
        best_key = max(analysis_results.keys(), key=lambda k: analysis_results[k]["score"])

        overall_score_text.value = str(avg_score)
        overall_score_text.color = get_score_class(avg_score)
        best_lang_text.value = f"{LANGS[best_key]['icon']}  {LANGS[best_key]['name']}"

        fill_metrics_table()
        create_charts()

        results_column.controls.clear()
        results_column.controls.extend([
            ft.Row([
                ft.Card(ft.Container(ft.Column([overall_score_text, ft.Text("Puntuación General"), ft.Text("Descripción: eficiencia simulada")]), padding=16)),
                ft.Card(ft.Container(ft.Column([best_lang_text, ft.Text("Lenguaje Más Eficiente")]), padding=16)),
            ], alignment="spaceBetween"),
            ft.Row([ft.Container(bar_chart, expand=1), ft.Container(radar_chart, expand=1)], spacing=12),
            ft.Text("Métricas por lenguaje", weight="w600"),
            table_rows
        ])
        results_column.visible = True
        page.update()

    calculate_btn.on_click = lambda e: ft.async_task(on_calculate(e))

    page.add(
        header,
        ft.Container(height=20),
        ft.Container(ft.Column([cards_wrap]), padding=8),
        ft.Container(height=12),
        ft.Row([calculate_btn], alignment="center"),
        ft.Container(height=16),
        results_column
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main, upload_dir="uploads")
