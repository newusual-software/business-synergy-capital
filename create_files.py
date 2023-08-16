# create_files.py
import os

file_names = [
    "sba-usda-loans",
    "revenue-based-loan-programs",
    "unsecured-lines-of-credit",
    "accounts-receivable-factoring",
    "asset-based-lending",
    "purchase-order-financing",
    "leasing",
    "transitional-financing",
    "startup-leasing",
    "conventional-business-loan",
    "fha-hud-loans",
    "fannie-may-loans",
    "conduit-cmbs",
    "freddie-mac-loans",
    "ctl-loans",
    "bridge-loans-nationwide",
    "small-balance-bridge-loans",
    "stated-loan-program",
    "land-loans",
    "sfr-acquisition-credit",
    "transitional-borrower",
    "sfr-landlord-financing",
    "agricultural-advisory-services",
    "franchise-loan-program",
    "consumer-finance-program",
    "business-payment-solutions",
    "leverage-line",
    "non-profit-financing",
    "consumer-leasing-program",
    "car-dealership-program",
    "agricultural-loans-real-estate",
    "agricultural-loans-operating-equipment",
    "agricultural-investor-loan",
    "agribusiness-loan-program",
]

for file_name in file_names:
    title = file_name.replace('-', ' ').capitalize()
    html_content = f'''<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title.capitalize()}</title>
    
    <style>
      * {{
        margin: 0;
        padding: 0;
      }}
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
            width: 100%;
        }}
        header {{
            width: 100%;
            height: 50vh;
            background-color: #1b1f29;
            color: #fff;
        }}
        main {{
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }}
        h1 {{
            color: #004080;
            margin-bottom: 1rem;
        }}
        h2 {{
            color: #004080;
            margin-top: 1.5rem;
        }}
        strong {{
            color: #000;
        }}
        p {{
            margin: 0.5rem 0;
        }}
        .headerContent {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 5rem;
            width: 70%;
            gap: 1rem;
            z-index: 999;
            font-size: 3rem;
            font-family: "Merriweather", serif;
            font-weight: bold;
            text-align: center;
            color: #fff;
        }}
        .btn-container {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .btn {{
            margin-top: 1.5rem;
            background: #004080;
            text-transform: uppercase;
            padding: 0.8rem 1.5rem;
            font-weight: 500;
            letter-spacing: 2px;
            border-radius: 5px;
            color: #fff;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            border: none;
            outline: none;
            cursor: pointer;
        }}
        .applyBtn {{
            background: transparent;
            border: 2px solid white;
            text-transform: uppercase;
            padding: 0.8rem 1.5rem;
            font-weight: bold;
            border-radius: 5px;
            color: #fff;
        }}
        .applyBtn:hover {{
            background-color: #fff;
            color: #000;
        }}
        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: transparent;
            border-bottom: 1px solid #b1adad;
            color: #fff;
            padding: 1.5rem 2rem;
        }}
        .logo img {{
            width: 50px;
            height: 50px;
        }}
        .menu {{
            list-style: none;
            display: flex;
            gap: 20px;
        }}
        .menu li {{
            position: relative;
        }}
        .menu a {{
            font-family: "Roboto", sans-serif;
            font-weight: medium;
            text-decoration: none;
            color: #fff;
        }}
        .menu a i {{
            margin-left: 5px;
        }}
        .dropdown-menu {{
            display: none;
            position: absolute;
            background-color: #333;
            list-style: none;
            width: 15rem;
            height: 25rem;
            overflow-y: auto;
            padding: 10px 0;
            top: 100%;
            left: 0;
        }}
        .dropdown:hover .dropdown-menu {{
            display: block;
        }}
        .dropdown-menu > li {{
            padding: 0.5rem 0;
            border-bottom: 2px solid #fff;
            padding-left: 0.5rem;
        }}
        .dropdown-menu > li > a {{
            margin-top: 2rem;
        }}
    </style>
  </head>
  <body>
    <header>
      <nav class="navbar">
        <div class="logo">
          <img src="./img/logo.png" alt="Site Logo" />
        </div>
        <ul class="menu">
          <li><a href="./index.html">Home</a></li>
          <li><a href="./about.html">About</a></li>
          <li class="dropdown">
            <a href="#">Loan Program <i class="fas fa-chevron-down"></i></a>
            <ul class="dropdown-menu">
              <li><a href="./sba-usda-loans.html">SBA & USDA Loans</a></li>
              <li>
                <a href="./revenue-based-loan-programs.html"
                  >Revenue Based Small Dollar Loan Programs</a
                >
              </li>
              <li>
                <a href="./unsecured-lines-of-credit.html"
                  >Business Unsecured Lines of Credit</a
                >
              </li>
              <li>
                <a href="./accounts-receivable-factoring.html"
                  >Accounts Receivable Factoring</a
                >
              </li>
              <li>
                <a href="./asset-based-lending.html"
                  >ABL (Asset Based Lending for Working Capital LOC)</a
                >
              </li>
              <li>
                <a href="./purchase-order-financing.html"
                  >Purchase Order Financing</a
                >
              </li>
              <li><a href="./leasing.html">Leasing</a></li>
              <li>
                <a href="./transitional-financing.html"
                  >Transitional Loan Financing for Businesses</a
                >
              </li>
              <li>
                <a href="./startup-leasing.html">Startup Leasing Program</a>
              </li>
              <li>
                <a href="./conventional-business-loan.html"
                  >Conventional Business Loan Program</a
                >
              </li>
              <li>
                <a href="./fha-hud-loans.html"
                  >FHA-HUD (221 d4 / 223 f / 223 a7 / 232)</a
                >
              </li>
              <li><a href="./fannie-may-loans.html">Fannie May</a></li>
              <li><a href="./conduit-cmbs.html">Conduit (CMBS)</a></li>
              <li><a href="./freddie-mac-loans.html">Freddie Mac</a></li>
              <li>
                <a href="./ctl-loans.html">CTL (Credit Tenant Lease/NNN)</a>
              </li>
              <li>
                <a href="./bridge-loans-nationwide.html"
                  >Bridge Loans Nationwide</a
                >
              </li>
              <li>
                <a href="./small-balance-bridge-loans.html"
                  >Small Balance Bridge Loans Nationwide</a
                >
              </li>
              <li>
                <a href="./stated-loan-program.html">Stated Loan Program</a>
              </li>
              <li><a href="./land-loans.html">Land Loans</a></li>
              <li>
                <a href="./sfr-acquisition-credit.html"
                  >SFR Acquisition Credit Program</a
                >
              </li>
              <li>
                <a href="./transitional-borrower.html"
                  >Transitional Borrower Program</a
                >
              </li>
              <li>
                <a href="./sfr-landlord-financing.html"
                  >SFR Landlord Financing Program</a
                >
              </li>
              <li>
                <a href="./agricultural-advisory-services.html"
                  >Agricultural Advisory Services</a
                >
              </li>
              <li>
                <a href="./franchise-loan-program.html"
                  >Conventional Franchise Loan Program</a
                >
              </li>
              <li>
                <a href="./consumer-finance-program.html"
                  >Consumer Finance Program for Merchants</a
                >
              </li>
              <li>
                <a href="./business-payment-solutions.html"
                  >Business Payment Solutions</a
                >
              </li>
              <li>
                <a href="./leverage-line.html">Leverage Line (Stock Loan)</a>
              </li>
              <li>
                <a href="./non-profit-financing.html"
                  >Non-Profit Financing Program</a
                >
              </li>
              <li>
                <a href="./consumer-leasing-program.html"
                  >Consumer Leasing Program for Merchants</a
                >
              </li>
              <li>
                <a href="./car-dealership-program.html"
                  >Car Dealership Program</a
                >
              </li>
              <li>
                <a href="./agricultural-loans-real-estate.html"
                  >Agricultural Loans - Real Estate</a
                >
              </li>
              <li>
                <a href="./agricultural-loans-operating-equipment.html"
                  >Agricultural Loans - Operating & Equipment</a
                >
              </li>
              <li>
                <a href="./agricultural-investor-loan.html"
                  >Agricultural Investor Loan Program</a
                >
              </li>
              <li>
                <a href="./agribusiness-loan-program.html"
                  >Agricultural Agribusiness Loan Program</a
                >
              </li>
            </ul>
          </li>

          <li><a href="./contact.html">Contact Us</a></li>
        </ul>
        <div>
          <button class="applyBtn">Apply Now</button>
        </div>
      </nav>
      <div class="headerContent">{title.capitalize()}</div>
    </header>
    <main>
      <section>
        <h2>For all Owner Occupied Businesses</h2>
        <p>
          <strong
            >a) Purchase, Refinance, Rehab, Construction, Working Capital,
            Equipment</strong
          >
        </p>
        <p><strong>b) 80% to 90% Financing</strong></p>
        <p><strong>c) Rates Start in the Mid to High 5’s</strong></p>
        <p>
          <strong
            >d) Variable/Fixed (1st) and Fixed (2nd) Pricing Available</strong
          >
        </p>
        <p>
          <strong
            >e) 10 Year Term (1st) / 10 or 20 Year Amortization (2nd)</strong
          >
        </p>
        <p><strong>f) Declining Pre-Payment Penalty</strong></p>
        <p><strong>g) Recourse</strong></p>
        <p>
          <strong
            >h) Min Loan Amount $350,000 - Max Loan Amount $5,000,000</strong
          >
        </p>
      </section>
      <section>
        <h2>For all Owner Occupied Businesses</h2>
        <p><strong>a) Fixed Asset Purchase, Construction</strong></p>
        <p>
          <strong
            >b) 75% to 90% Financing (can go higher with professionals)</strong
          >
        </p>
        <p><strong>c) Max Interest Rate - Prime + 2.75%</strong></p>
        <p>
          <strong>d) 10 to 25 Year Term / 10 to 25 Year Amortization</strong>
        </p>
        <p>
          <strong
            >e) Prepayment Real Estate - 5/3/1 - No Prepayment &lt; 15 Year
            Term</strong
          >
        </p>
        <p><strong>f) Recourse</strong></p>
        <p>
          <strong
            >g) Min Loan Amount $500,000 - Max Loan Amount $5,000,000</strong
          >
        </p>
      </section>
      <div class="btn-container">
        <button class="btn">
          Apply Now
          <span class="svg-container">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="1em"
              viewBox="0 0 448 512"
            >
              <style>
                .custom-path {{
                  fill: #000;
                }}
              </style>
              <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
              <path
                class="custom-path"
                d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"
              />
            </svg>
          </span>
        </button>
      </div>
    </main>
  </body>
</html>
'''

    file_path = f"./{file_name}.html"
    with open(file_path, "w") as file:
        file.write(html_content)
