# 📊 E-commerce Sales Dashboard

This project presents a dashboard-style visualization of mock e-commerce sales data. The goal is to simulate and analyze revenue trends and patterns across product categories and regions.

## 🚀 Objective

Build a comprehensive set of visualizations using Python to explore and present insights from e-commerce sales data.

---

## 📁 Dataset

A synthetic dataset is generated with 100+ rows using `numpy` and `pandas`. The dataset contains the following columns:

- `Order_Date`: The date of the order.
- `Product_Category`: The category of the product sold.
- `Revenue`: Revenue generated from the sale.
- `Region`: The geographical region where the sale occurred.

---

## 🛠️ Features & Tasks

### ✅ Data Preparation

- Convert `Order_Date` to datetime format.
- Extract `Month` from the order date for monthly aggregation.

### 📈 Visualizations

All visualizations are created using `matplotlib`, `seaborn`, and `pandas`. Layouts are structured using subplots or separate figures.

1. **Line Chart** - Monthly revenue trend.
2. **Bar Chart** - Total revenue by product category.
3. **Pie Chart** - Revenue distribution by region.
4. **Heatmap** - Cross-tab of product categories vs. regions.
5. **Box Plot** - Revenue distribution per category.

### 📐 Styling

- Custom styling using `plt.style.use('seaborn')`.
- All plots include descriptive titles, axis labels, and legends where appropriate.

---

## 📊 Sample Visuals

(Insert images or add links to visualizations if available)

---

## 📦 Dependencies

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn

Install them with:

```bash
pip install pandas numpy matplotlib seaborn
