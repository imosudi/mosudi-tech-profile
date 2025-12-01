
      document.addEventListener('DOMContentLoaded', function() {
        new Typed("#typed-text", {
          strings: ["Network Infrastructure", "Full-Stack Software Developer", "IoT Specialist", "Edge Systems Researcher", "Tech Support Specialist"], //* "AI-Driven Innovator"],*/
          typeSpeed: 60,
          backSpeed: 35,
          backDelay: 1500,
          loop: true
        });
      });


      function showToast(message, type="success") {
        Toastify({
          text: message,
          duration: 3000,
          gravity: "top",
          position: "right",
          backgroundColor: type === "success" ? "#198754" : "#dc3545",
        }).showToast();
      }


      document.addEventListener("DOMContentLoaded", function() {
        VanillaTilt.init(document.querySelectorAll(".card"), {
          max: 10,
          speed: 400,
          glare: true,
          "max-glare": 0.2
        });
      });

      window.setTimeout(function() {
        window.location.reload();
    }, 1800000); // 30 minutes = 30 * 60 * 1000 = 1,800,000 milliseconds