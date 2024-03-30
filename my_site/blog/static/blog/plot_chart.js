// plot_chart.js

function createChart(salesData) {
    // Extract dates and sales data for each shop
    const dates = salesData.shopA.map(entry => entry.date);
    const shopASales = salesData.shopA.map(entry => entry.sales);
    const shopBSales = salesData.shopB.map(entry => entry.sales);
  
    // Create the chart
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