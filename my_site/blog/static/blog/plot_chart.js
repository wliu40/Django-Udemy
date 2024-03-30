// plot_chart.js

// Sample data
const salesData = {
    shopA: [
      { date: '2023-03-01', sales: 100 },
      { date: '2023-03-02', sales: 150 },
      { date: '2023-03-03', sales: 120 },
      // ... more data points for Shop A
    ],
    shopB: [
      { date: '2023-03-01', sales: 80 },
      { date: '2023-03-02', sales: 200 },
      { date: '2023-03-03', sales: 180 },
      // ... more data points for Shop B
    ],
  };
  
  // Extract dates and sales data for each shop
  const dates = salesData.shopA.map(entry => entry.date);
  const shopASales = salesData.shopA.map(entry => entry.sales);
  const shopBSales = salesData.shopB.map(entry => entry.sales);
  
  // Create the chart
  function createChart() {
    const ctx = document.getElementById('salesChart').getContext('2d');
  
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [
          {
            label: 'Shop A',
            data: shopASales,
            borderColor: 'blue',
            fill: false,
          },
          {
            label: 'Shop B',
            data: shopBSales,
            borderColor: 'red',
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Date',
            },
          },
          y: {
            display: true,
            title: {
              display: true,
              text: 'Number of Sales',
            },
          },
        },
      },
    });
  }
  
  // Call the createChart function when the page loads
  window.onload = createChart;