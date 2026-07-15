import random

def generate_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxury Wedding Chauffeur Services London</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        champagne: '#F7E7CE',
                        gold: '#D4AF37',
                        pearl: '#FDFBF7',
                        charcoal: '#333333'
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', 'serif'],
                        sans: ['Montserrat', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #FDFBF7; color: #333333; overflow-x: hidden; }
        .section-container { min-height: 100vh; display: flex; flex-direction: column; justify-content: center; padding: 4rem 2rem; border-bottom: 1px solid #F7E7CE; }
        .image-placeholder { background-color: #eee; background-size: cover; background-position: center; }
        .hide { opacity: 0; }
    </style>
</head>
<body class="font-sans antialiased">
    <nav class="fixed top-0 w-full bg-pearl/90 backdrop-blur z-50 py-4 px-8 border-b border-champagne flex justify-between items-center" id="navbar">
        <div class="font-serif text-2xl font-bold text-gold">London Elegance</div>
        <div class="hidden md:flex gap-6 text-sm tracking-widest uppercase">
            <a href="#" class="hover:text-gold transition-colors">Home</a>
            <a href="#" class="hover:text-gold transition-colors">Fleet</a>
            <a href="#" class="hover:text-gold transition-colors">Services</a>
            <a href="#" class="hover:text-gold transition-colors">Contact</a>
        </div>
    </nav>
    <main class="mt-20">
"""

    sections = []

    for i in range(1, 101):
        img_url = f"https://picsum.photos/seed/luxury{i}/800/600"

        section_html = f"""
        <!-- Section {i} -->
        <section class="section-container relative" id="section-{i}">
            <div class="max-w-6xl mx-auto w-full">
                <div class="text-xs tracking-widest text-gold mb-2 uppercase font-semibold">Section {i} / 100</div>
        """

        anim_type = ""
        js_code = ""

        if 1 <= i <= 10:
            anim_type = "Hero Reveal Animation (GSAP from/to)"
            section_html += f"""
                <h1 class="font-serif text-5xl md:text-7xl mb-6 hero-title-{i} hide">Luxury Wedding Chauffeur</h1>
                <p class="text-xl mb-8 hero-text-{i} hide">Arrive in unparalleled style on your special day in London.</p>
                <div class="hero-image-{i} w-full h-96 rounded-lg image-placeholder hide" style="background-image: url('{img_url}')"></div>
                <div class="mt-4 text-sm text-gray-500 italic">Library used: GSAP. This section uses basic `gsap.fromTo` to create a staggered entry of title, text, and image when they scroll into view.</div>
            """
            js_code = f"""
                gsap.fromTo(".hero-title-{i}", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".hero-text-{i}", {{y: 50, opacity: 0}}, {{y: 0, opacity: 1, duration: 1, delay: 0.2, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".hero-image-{i}", {{scale: 0.9, opacity: 0}}, {{scale: 1, opacity: 1, duration: 1.5, delay: 0.4, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
            """
        elif 11 <= i <= 20:
            anim_type = "Text Split & Stagger (GSAP)"
            section_html += f"""
                <h2 class="font-serif text-4xl mb-4 text-reveal-{i} hide">Elegance in Every Detail</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center mt-8">
                    <p class="text-lg leading-relaxed text-body-{i} hide">Our meticulously maintained fleet ensures your journey is as flawless as your destination. We provide a bespoke service tailored to your exact requirements.</p>
                    <div class="h-64 rounded-lg image-placeholder text-img-{i} hide" style="background-image: url('{img_url}')"></div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic">Library used: GSAP. The text fades and slides in from the left, while the image fades in from the right.</div>
            """
            js_code = f"""
                gsap.fromTo(".text-reveal-{i}", {{x: -50, opacity: 0}}, {{x: 0, opacity: 1, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
                gsap.fromTo(".text-body-{i}", {{x: -30, opacity: 0}}, {{x: 0, opacity: 1, duration: 1, delay: 0.2, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
                gsap.fromTo(".text-img-{i}", {{x: 50, opacity: 0}}, {{x: 0, opacity: 1, duration: 1, delay: 0.4, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
            """
        elif 21 <= i <= 30:
            anim_type = "Image Parallax Effect (GSAP ScrollTrigger scrub)"
            section_html += f"""
                <h2 class="font-serif text-4xl mb-8 text-center parallax-title-{i} hide">A Journey to Remember</h2>
                <div class="overflow-hidden h-96 rounded-xl relative">
                    <div class="parallax-img-{i} w-full h-[130%] absolute -top-[15%] left-0 image-placeholder" style="background-image: url('{img_url}')"></div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP ScrollTrigger. The image moves at a different speed than the scroll (parallax) using `scrub: true`.</div>
            """
            js_code = f"""
                gsap.fromTo(".parallax-title-{i}", {{opacity: 0, y: 30}}, {{opacity: 1, y: 0, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.to(".parallax-img-{i}", {{
                    yPercent: 30,
                    ease: "none",
                    scrollTrigger: {{
                        trigger: "#section-{i}",
                        start: "top bottom",
                        end: "bottom top",
                        scrub: true
                    }}
                }});
            """
        elif 31 <= i <= 40:
            anim_type = "Staggered Cards (GSAP stagger)"
            section_html += f"""
                <h2 class="font-serif text-4xl mb-12 text-center fleet-title-{i} hide">Our Exclusive Fleet</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="bg-white p-6 rounded-lg shadow-lg fleet-card-{i} hide border border-champagne">
                        <div class="h-40 mb-4 rounded image-placeholder" style="background-image: url('https://picsum.photos/seed/car{i}1/400/300')"></div>
                        <h3 class="font-serif text-xl font-bold mb-2">Rolls Royce Phantom</h3>
                        <p class="text-sm">The pinnacle of luxury.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg fleet-card-{i} hide border border-champagne">
                        <div class="h-40 mb-4 rounded image-placeholder" style="background-image: url('https://picsum.photos/seed/car{i}2/400/300')"></div>
                        <h3 class="font-serif text-xl font-bold mb-2">Bentley Mulsanne</h3>
                        <p class="text-sm">Classic British elegance.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-lg fleet-card-{i} hide border border-champagne">
                        <div class="h-40 mb-4 rounded image-placeholder" style="background-image: url('https://picsum.photos/seed/car{i}3/400/300')"></div>
                        <h3 class="font-serif text-xl font-bold mb-2">Mercedes S-Class</h3>
                        <p class="text-sm">Modern sophistication.</p>
                    </div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP. The cards animate in sequentially using GSAP's `stagger` feature when the section is reached.</div>
            """
            js_code = f"""
                gsap.fromTo(".fleet-title-{i}", {{opacity: 0, y: -20}}, {{opacity: 1, y: 0, duration: 0.8, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".fleet-card-{i}",
                    {{opacity: 0, y: 50, scale: 0.9}},
                    {{opacity: 1, y: 0, scale: 1, duration: 0.8, stagger: 0.2, ease: "back.out(1.7)", scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}}
                );
            """
        elif 41 <= i <= 50:
            anim_type = "Icon Pop-in (GSAP scale & elastic ease)"
            section_html += f"""
                <h2 class="font-serif text-3xl mb-10 text-center feature-title-{i} hide">Why Choose Us</h2>
                <div class="flex flex-wrap justify-center gap-12">
                    <div class="text-center feature-item-{i} hide">
                        <div class="w-20 h-20 mx-auto bg-champagne rounded-full flex items-center justify-center text-gold text-3xl mb-4 shadow-md"><i class="fas fa-crown"></i></div>
                        <h4 class="font-bold">Premium Service</h4>
                    </div>
                    <div class="text-center feature-item-{i} hide">
                        <div class="w-20 h-20 mx-auto bg-champagne rounded-full flex items-center justify-center text-gold text-3xl mb-4 shadow-md"><i class="fas fa-user-tie"></i></div>
                        <h4 class="font-bold">Professional Drivers</h4>
                    </div>
                    <div class="text-center feature-item-{i} hide">
                        <div class="w-20 h-20 mx-auto bg-champagne rounded-full flex items-center justify-center text-gold text-3xl mb-4 shadow-md"><i class="fas fa-clock"></i></div>
                        <h4 class="font-bold">Punctuality</h4>
                    </div>
                </div>
                <div class="mt-12 text-sm text-gray-500 italic text-center">Library used: GSAP. Icons scale up with an elastic easing for a playful yet luxurious pop-in effect.</div>
            """
            js_code = f"""
                gsap.fromTo(".feature-title-{i}", {{opacity: 0}}, {{opacity: 1, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 85%"}}}});
                gsap.fromTo(".feature-item-{i}",
                    {{opacity: 0, scale: 0}},
                    {{opacity: 1, scale: 1, duration: 1, stagger: 0.15, ease: "elastic.out(1, 0.5)", scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}}
                );
            """
        elif 51 <= i <= 60:
            anim_type = "Testimonial Slide (GSAP)"
            section_html += f"""
                <h2 class="font-serif text-3xl mb-8 text-center testi-title-{i} hide">What Our Clients Say</h2>
                <div class="max-w-3xl mx-auto bg-white p-8 rounded-xl shadow-xl border border-champagne testi-box-{i} hide relative">
                    <i class="fas fa-quote-left text-4xl text-champagne absolute top-4 left-4 opacity-50"></i>
                    <p class="text-xl italic text-center mb-6 relative z-10">"The service was absolutely impeccable. The driver was early, polite, and the Rolls Royce was stunning. Made our London wedding perfect!"</p>
                    <div class="text-center font-bold text-gold uppercase tracking-wider">- Sarah & James</div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP. The testimonial box slides up and fades in with a smooth power-out ease.</div>
            """
            js_code = f"""
                gsap.fromTo(".testi-title-{i}", {{opacity: 0, y: -20}}, {{opacity: 1, y: 0, duration: 0.8, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".testi-box-{i}", {{opacity: 0, y: 100, rotation: -2}}, {{opacity: 1, y: 0, rotation: 0, duration: 1, ease: "power3.out", scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
            """
        elif 61 <= i <= 70:
            anim_type = "Package Flip or Scale (GSAP)"
            section_html += f"""
                <h2 class="font-serif text-4xl mb-10 text-center pkg-title-{i} hide">Wedding Packages</h2>
                <div class="flex flex-col md:flex-row justify-center gap-8">
                    <div class="flex-1 bg-white p-8 rounded-lg shadow border border-gray-100 pkg-card-{i} hide flex flex-col items-center">
                        <h3 class="font-serif text-2xl font-bold mb-4">Silver</h3>
                        <div class="text-3xl font-bold text-gold mb-6">£399</div>
                        <ul class="text-center mb-8 space-y-2">
                            <li>3 Hours Service</li>
                            <li>Ribbons & Bows</li>
                            <li>Professional Chauffeur</li>
                        </ul>
                        <button class="px-6 py-2 bg-charcoal text-white rounded hover:bg-gold transition-colors mt-auto">Enquire</button>
                    </div>
                    <div class="flex-1 bg-charcoal text-white p-8 rounded-lg shadow-2xl border border-gold pkg-card-{i} transform scale-105 hide flex flex-col items-center relative overflow-hidden">
                        <div class="absolute top-0 right-0 bg-gold text-xs font-bold px-3 py-1 rounded-bl-lg">POPULAR</div>
                        <h3 class="font-serif text-2xl font-bold mb-4">Gold</h3>
                        <div class="text-3xl font-bold text-gold mb-6">£599</div>
                        <ul class="text-center mb-8 space-y-2">
                            <li>5 Hours Service</li>
                            <li>Complimentary Champagne</li>
                            <li>Red Carpet on Arrival</li>
                        </ul>
                        <button class="px-6 py-2 bg-gold text-charcoal font-bold rounded hover:bg-white transition-colors mt-auto">Enquire</button>
                    </div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP. The pricing cards rotate into place along the Y-axis (3D flip effect) as you scroll.</div>
            """
            js_code = f"""
                gsap.fromTo(".pkg-title-{i}", {{opacity: 0}}, {{opacity: 1, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".pkg-card-{i}",
                    {{opacity: 0, rotationY: 90}},
                    {{opacity: 1, rotationY: 0, duration: 1, stagger: 0.2, ease: "power2.out", scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}}
                );
            """
        elif 71 <= i <= 80:
            anim_type = "Split Layout (GSAP)"
            section_html += f"""
                <div class="flex flex-col md:flex-row gap-12 items-center">
                    <div class="w-full md:w-1/2 about-img-{i} hide">
                        <div class="w-full h-80 rounded-2xl image-placeholder shadow-2xl" style="background-image: url('{img_url}')"></div>
                    </div>
                    <div class="w-full md:w-1/2 about-text-{i} hide">
                        <h2 class="font-serif text-4xl mb-6">Our Legacy</h2>
                        <p class="text-lg mb-4">With over 20 years of providing luxury chauffeur services in London, we understand the importance of perfection on your wedding day.</p>
                        <p class="text-lg">Every chauffeur is hand-picked, every vehicle is meticulously valeted, ensuring an experience that is truly second to none.</p>
                    </div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic">Library used: GSAP. The image slides in from the left and text from the right, meeting in the middle.</div>
            """
            js_code = f"""
                gsap.fromTo(".about-img-{i}", {{opacity: 0, x: -100}}, {{opacity: 1, x: 0, duration: 1, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
                gsap.fromTo(".about-text-{i}", {{opacity: 0, x: 100}}, {{opacity: 1, x: 0, duration: 1, delay: 0.2, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}});
            """
        elif 81 <= i <= 90:
            anim_type = "Masonry/Grid Stagger (GSAP)"
            section_html += f"""
                <h2 class="font-serif text-4xl mb-8 text-center gal-title-{i} hide">Moments Captured</h2>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div class="h-40 rounded image-placeholder gal-item-{i} hide" style="background-image: url('https://picsum.photos/seed/gal{i}1/300/300')"></div>
                    <div class="h-40 rounded image-placeholder gal-item-{i} hide" style="background-image: url('https://picsum.photos/seed/gal{i}2/300/300')"></div>
                    <div class="h-40 rounded image-placeholder gal-item-{i} hide" style="background-image: url('https://picsum.photos/seed/gal{i}3/300/300')"></div>
                    <div class="h-40 rounded image-placeholder gal-item-{i} hide" style="background-image: url('https://picsum.photos/seed/gal{i}4/300/300')"></div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP. The gallery images fade in with a random scatter effect using `stagger: {{ amount: 1, from: "random" }}`.</div>
            """
            js_code = f"""
                gsap.fromTo(".gal-title-{i}", {{opacity: 0, scale: 0.8}}, {{opacity: 1, scale: 1, duration: 0.8, scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.fromTo(".gal-item-{i}",
                    {{opacity: 0, scale: 0.5, rotation: 10}},
                    {{opacity: 1, scale: 1, rotation: 0, duration: 0.8, stagger: {{amount: 1, from: "random"}}, scrollTrigger: {{trigger: "#section-{i}", start: "top 75%"}}}}
                );
            """
        else:
            anim_type = "CTA Attention (GSAP)"
            section_html += f"""
                <div class="bg-champagne p-12 rounded-3xl text-center cta-box-{i} hide relative overflow-hidden">
                    <div class="absolute inset-0 opacity-10 bg-cover bg-center" style="background-image: url('{img_url}')"></div>
                    <div class="relative z-10">
                        <h2 class="font-serif text-4xl mb-4 text-gold">Ready to Book?</h2>
                        <p class="text-xl mb-8 max-w-2xl mx-auto">Secure your luxury wedding car today and ensure your London wedding is unforgettable.</p>
                        <button class="px-8 py-3 bg-charcoal text-white text-lg rounded-full hover:bg-gold transition-colors cta-btn-{i}">Contact Us Now</button>
                    </div>
                </div>
                <div class="mt-8 text-sm text-gray-500 italic text-center">Library used: GSAP. The CTA box grows from the center, and the button has a continuous pulse animation.</div>
            """
            js_code = f"""
                gsap.fromTo(".cta-box-{i}", {{opacity: 0, scale: 0.8, borderRadius: "100px"}}, {{opacity: 1, scale: 1, borderRadius: "24px", duration: 1.2, ease: "power3.inOut", scrollTrigger: {{trigger: "#section-{i}", start: "top 80%"}}}});
                gsap.to(".cta-btn-{i}", {{scale: 1.05, duration: 0.8, repeat: -1, yoyo: true, ease: "sine.inOut"}});
            """

        section_html += f"""
            </div>
        </section>
        """

        sections.append({
            "html": section_html,
            "js": js_code
        })

    for s in sections:
        html += s["html"]

    html += """
    </main>
    <footer class="bg-charcoal text-white py-12 text-center border-t-4 border-gold">
        <div class="font-serif text-3xl text-gold mb-4">London Elegance</div>
        <p class="mb-4">Luxury Wedding Chauffeur Services</p>
        <p class="text-sm text-gray-400">&copy; 2024 London Elegance. All rights reserved.</p>
    </footer>

    <script>
        // Register GSAP ScrollTrigger
        gsap.registerPlugin(ScrollTrigger);

        // Navbar blur on scroll
        window.addEventListener('scroll', () => {
            const nav = document.getElementById('navbar');
            if (window.scrollY > 50) {
                nav.classList.add('shadow-md');
            } else {
                nav.classList.remove('shadow-md');
            }
        });

        // Initialize animations for all 100 sections
"""

    for s in sections:
        html += s["js"]

    html += """
    </script>
</body>
</html>
"""

    with open("index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()
    print("Successfully generated index.html with 100 sections!")
