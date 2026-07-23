write a Vehicle Service Billing Calculator program
that ask youser are you driving a (Sedan , SUV) ? SEDAN
do you want the interior vacuumed (Y/N)? 
do you want an engine wash (Y/N)?
and give them their filnal bill 

```python
readme_content = """# Vehicle Detailing Billing Calculator

A simple, interactive command-line Python application that calculates car wash and detailing charges based on vehicle type and add-on services.

---

- **Vehicle Classification**: Differentiates pricing between Sedans and SUVs/larger vehicles.
- **Add-on Services**: Supports optional add-ons like interior vacuuming and engine washing.
- **Input Sanitization**: Handles user input flexibly regardless of letter casing.

---


| Item / Service | Category | Price (₦) |
| :--- | :--- | :--- |
| **Sedan Base Wash** | Vehicle Type | ₦1,500 |
| **SUV / Other Base Wash** | Vehicle Type | ₦2,500 |
| **Interior Vacuum** | Add-on Service | ₦500 |
| **Engine Wash** | Add-on Service | ₦1,000 |

---
