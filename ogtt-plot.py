import matplotlib.pyplot as plt
import seaborn as sns

# Twoje wyniki badań
czas = [0, 60, 120]  # minuty
glukoza = [95, 161, 116]     # mg/dl – przykładowe dane
insulina = [15.4, 167, 92.6]      # µIU/ml – opcjonalnie

# Wartości referencyjne (orientacyjne)
glukoza_ref = [85, 120, 100]  # referencyjne poziomy glukozy (mg/dl)
insulina_ref = [5, 50, 30]    # referencyjne poziomy insuliny (µU/ml)


# Obliczenie HOMA-IR (użyj wartości na czczo)
glukoza_na_czczo = glukoza[0]  # wartość na czczo (0 minut)
insulina_na_czczo = insulina[0]  # wartość na czczo (0 minut)

homa_ir = (glukoza_na_czczo * insulina_na_czczo) / 405

# Konfiguracja stylu
sns.set_style("whitegrid")
font_title = 14
font_labels = 12
font_ticks = 10
font_legend = 10

# WYKRES 1 – Glukoza
fig1, ax1 = plt.subplots(figsize=(6, 6))  # bardziej kwadratowy
ax1.plot(czas, glukoza, label="Glukoza (mg/dl)", marker='o', color='blue', markersize=6)
ax1.plot(czas, glukoza_ref, label="Referencyjna glukoza", linestyle='--', color='green')
ax1.set_title("Krzywa glukozowa (OGTT)", fontsize=font_title)
ax1.set_xlabel("Czas (minuty)", fontsize=font_labels)
ax1.set_ylabel("Poziom glukozy (mg/dl)", fontsize=font_labels)
ax1.tick_params(axis='both', labelsize=font_ticks)
ax1.legend(fontsize=font_legend, loc='upper right')
ax1.grid(True)
plt.tight_layout()
plt.show()

# WYKRES 2 – Insulina
fig2, ax2 = plt.subplots(figsize=(6, 6))  # bardziej kwadratowy
ax2.plot(czas, insulina, label="Insulina (µU/ml)", marker='o', color='orange', markersize=6)
ax2.plot(czas, insulina_ref, label="Referencyjna insulina", linestyle='--', color='purple')
ax2.set_title("Krzywa insulinowa (OGTT)", fontsize=font_title)
ax2.set_xlabel("Czas (minuty)", fontsize=font_labels)
ax2.set_ylabel("Poziom insuliny (µU/ml)", fontsize=font_labels)
ax2.tick_params(axis='both', labelsize=font_ticks)
ax2.legend(fontsize=font_legend, loc='upper right')
ax2.text(0, max(insulina) + 10, f'HOMA-IR: {homa_ir:.2f}', fontsize=font_labels, color='black')
ax2.grid(True)
plt.tight_layout()
plt.show()

# Zapis wykresów
fig1.savefig("glukoza_ogtt_mob.png", dpi=150)
fig2.savefig("insulina_ogtt_mob.png", dpi=150)