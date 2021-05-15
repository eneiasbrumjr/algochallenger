(function () {
  "use strict";

  const API = "http://127.0.0.1:5000/calc";
  let headers = new Headers();
  headers.append("token", `${JSON.parse(localStorage.getItem("token"))}`);

  let customHeader = {
    method: "GET",
    headers: headers,
  };

  document.getElementById("graphics").style.display = "none";
  document.getElementById("loading").style.display = "block";

  const fetchApi = async () => {
    return await fetch(API, customHeader)
      .then((res) => res.json())
      .then((ress) => {
        document.getElementById("graphics").style.display = "block";
        document.getElementById("loading").style.display = "none";
        const mock = ress;

        let listTD = {
          x: JSON.parse(mock.list_td),
          type: "histogram",
        };
        let listTPD = {
          x: JSON.parse(mock.list_tpd),
          type: "histogram",
        };
        let listTPDWD = {
          x: JSON.parse(mock.list_tpdwd),
          type: "histogram",
        };
        let listTWQ = {
          x: JSON.parse(mock.list_twq),
          type: "histogram",
        };
         let listTWQLINE = {
           y: JSON.parse(mock.media_list),
           type: 'bar',
          // orientation: 'h',
          //  mode: "lines",
           
         };
         let listTWQLINEGeneral = {
          y: JSON.parse(mock.media_list_general),
          type: 'bar',
          // orientation: 'h',
          // mode: "lines",
          
        };
        let listTWQLINE100v = {
          y: JSON.parse(mock.media_list_100v),
          mode: 'lines+markers',
          //type: 'bar',
          // orientation: 'h',
          type: 'scatter',
          
        };


         var layout_linetwq = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            title: {
              text: 'Num da amostra',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Média no tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };

        var layout_linetwq_general = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            title: {
              text: 'Num da amostra',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Média no tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };

        var layout_datalListTWQ = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            
            title: {
              text:'Média no tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Freq. de amostras',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };
        var layout_linetwq_100v = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            range: [0, 100],
            
            title: {
              text: 'Num da amostra',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Média no tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };
        var layout_dataListTPDWD = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            
            title: {
              text: 'Tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Freq. de amostras',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };
        var layout_dataListTPD = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {

            title: {
              text: 'Tempo (s)',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Freq. de amostras',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };
        var layout_dataListTD = {
          // title: {
          //   text:'Plot Title',
          //   font: {
          //     family: 'Courier New, monospace',
          //     size: 24
          //   },
          //   xref: 'paper',
          //   x: 0.05,
          // },
          xaxis: {
            
            title: {
              text:'Tempo (s)' ,
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Freq. de amostras',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };






        let dataListTD = [listTD];
        let dataListTPD = [listTPD];
        let dataListTPDWD = [listTPDWD];
        let datalListTWQ = [listTWQ];
        let datalListMedia = [listTWQLINE];
        let datalListMediaGeneral = [listTWQLINEGeneral];
        let datalListMedia100v = [listTWQLINE100v];
        

        Plotly.newPlot("listTD", dataListTD, layout_dataListTPD);
        Plotly.newPlot("listTPD", dataListTPD, layout_dataListTPD);
        Plotly.newPlot("listTPDWD", dataListTPDWD, layout_dataListTPDWD);
        Plotly.newPlot("listTWQ", datalListTWQ, layout_datalListTWQ);
        Plotly.newPlot("listTWQLINE", datalListMedia, layout_linetwq);
        Plotly.newPlot("listTWQLINEGeneral", datalListMediaGeneral, layout_linetwq);
        Plotly.newPlot("listTWQLINE100v", datalListMedia100v, layout_linetwq_100v);


        let table = document.getElementById("table-metrics");
        let tableBody = table.querySelector("tbody");

        const dataMetrics = mock.metrics;

        tableBody.innerHTML = "";
        dataMetrics.map((item) => {
          var row = document.createElement("tr");

          var cell1 = document.createElement("td");
          cell1.appendChild(document.createTextNode(item["name"]));
          var cell2 = document.createElement("td");
          cell2.appendChild(document.createTextNode(item["min"]));
          var cell3 = document.createElement("td");
          cell3.appendChild(document.createTextNode(item["media"]));
          var cell4 = document.createElement("td");
          cell4.appendChild(document.createTextNode(item["standard_desviation"]));
          var cell5 = document.createElement("td");
          cell5.appendChild(document.createTextNode(item["max"]));
          var cell6 = document.createElement("td");
          cell6.appendChild(document.createTextNode(item["95%"]));
          var cell7 = document.createElement("td");
          cell7.appendChild(document.createTextNode(item["99%"]));


          row.appendChild(cell1);
          row.appendChild(cell2);
          row.appendChild(cell3);
          row.appendChild(cell4);
          row.appendChild(cell5);
          row.appendChild(cell6);
          row.appendChild(cell7);

          tableBody.appendChild(row);
        });
        return "Success";
      })
      .catch((err) => {
        console.error(err);
        return "Error";
      });
  };

  function lastUpdate() {
    const elTime = document.getElementById("time");
    const time = `${new Date().getHours()}:${new Date().getMinutes()}:${new Date().getSeconds()}`;
    elTime.textContent = time;
  }

  function fetchAll() {
    fetchApi().then((res) => {
      lastUpdate();

      if (res === "Success") {
        const interval = setInterval(() => {
          fetchAll();
          clearInterval(interval);
        }, 5000);
      }

      if (res === "Error") {
        document.getElementById("error-message").style.display = "block";

        setTimeout(() => {
          document.getElementById("error-message").style.display = "none";
        }, 10000);
      }
    });
  }

  fetchAll();

  // setInterval(async () => {

  // }, 5000);

  //   // Parse JSON string into object

  // }, 1000);
})();
