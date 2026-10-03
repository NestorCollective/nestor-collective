# -*- coding: utf-8 -*-
"""Genera /it/index.html y /es/index.html a partir de index.html (ingles, el maestro).

Uso:  python _build/traducir.py
Cada entrada de T es (ingles, italiano, espanol). El ingles tiene que aparecer
tal cual en index.html: si cambia el maestro y una entrada no aparece, el script corta.
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, 'index.html')

T = [
# ---------- head ----------
('content="NESTOR Collective is an international non-profit community connecting university students through negotiation, strategic communication and leadership, while opening doors to exceptional experts, ideas and opportunities from around the world."',
 'content="NESTOR Collective e una comunita internazionale non profit che collega studenti universitari attraverso la negoziazione, la comunicazione strategica e la leadership, aprendo le porte a esperti, idee e opportunita straordinarie da tutto il mondo."'.replace('e una comunita','\u00e8 una comunit\u00e0').replace('opportunita','opportunit\u00e0'),
 'content="NESTOR Collective es una comunidad internacional sin fines de lucro que conecta a estudiantes universitarios a trav\u00e9s de la negociaci\u00f3n, la comunicaci\u00f3n estrat\u00e9gica y el liderazgo, y les abre las puertas a expertos, ideas y oportunidades excepcionales de todo el mundo."'),

# ---------- navegacion (aparecen en el header y en el pie) ----------
('<li><a href="#community">Community</a></li>', '<li><a href="#community">Comunit\u00e0</a></li>', '<li><a href="#community">Comunidad</a></li>'),
('<li><a href="#what">What we do</a></li>', '<li><a href="#what">Cosa facciamo</a></li>', '<li><a href="#what">Qu\u00e9 hacemos</a></li>'),
('<li><a href="#speakers">Speakers</a></li>', '<li><a href="#speakers">Speaker</a></li>', '<li><a href="#speakers">Speakers</a></li>'),
('<li><a href="#team">Team</a></li>', '<li><a href="#team">Team</a></li>', '<li><a href="#team">Equipo</a></li>'),
('<li><a href="#story">Story</a></li>', '<li><a href="#story">Storia</a></li>', '<li><a href="#story">Historia</a></li>'),
('<li><a href="#partners">Partners</a></li>', '<li><a href="#partners">Partner</a></li>', '<li><a href="#partners">Partners</a></li>'),
('>Join NESTOR <span class="arrow">\u2192</span></a>', '>Unisciti a NESTOR <span class="arrow">\u2192</span></a>', '>\u00danete a NESTOR <span class="arrow">\u2192</span></a>'),
('aria-label="Open menu"', 'aria-label="Apri il menu"', 'aria-label="Abrir el men\u00fa"'),
("btn.setAttribute('aria-label',open?'Close menu':'Open menu');", "btn.setAttribute('aria-label',open?'Chiudi il menu':'Apri il menu');", "btn.setAttribute('aria-label',open?'Cerrar el men\u00fa':'Abrir el men\u00fa');"),

# ---------- menu del celular ----------
('<small>01</small>Home</a>', '<small>01</small>Home</a>', '<small>01</small>Inicio</a>'),
('<small>02</small>The belief</a>', '<small>02</small>Il principio</a>', '<small>02</small>La convicci\u00f3n</a>'),
('<small>03</small>The community</a>', '<small>03</small>La comunit\u00e0</a>', '<small>03</small>La comunidad</a>'),
('<small>04</small>What we do</a>', '<small>04</small>Cosa facciamo</a>', '<small>04</small>Qu\u00e9 hacemos</a>'),
('<small>05</small>Speakers</a>', '<small>05</small>Speaker</a>', '<small>05</small>Speakers</a>'),
('<small>06</small>The people</a>', '<small>06</small>Le persone</a>', '<small>06</small>Las personas</a>'),
('<small>\u2014</small>Our story</a>', '<small>\u2014</small>La nostra storia</a>', '<small>\u2014</small>Nuestra historia</a>'),
('<small>07</small>Partners</a>', '<small>07</small>Partner</a>', '<small>07</small>Partners</a>'),
('<small>08</small>Join NESTOR</a>', '<small>08</small>Unisciti a NESTOR</a>', '<small>08</small>\u00danete a NESTOR</a>'),
('<p>Built by students \u00b7 6 countries \u00b7 3 continents</p>', '<p>Costruito da studenti \u00b7 6 paesi \u00b7 3 continenti</p>', '<p>Hecho por estudiantes \u00b7 6 pa\u00edses \u00b7 3 continentes</p>'),

# ---------- 01 hero ----------
("Tomorrow's leaders build <b>bridges</b> that change the world",
 'I leader di domani costruiscono <b>ponti</b> che cambiano il mondo',
 'Los l\u00edderes del ma\u00f1ana construyen <b>puentes</b> que cambian el mundo'),
('NESTOR Collective is an international non-profit community connecting university students through negotiation, strategic communication and leadership, while opening doors to exceptional experts, ideas and opportunities from around the world.</p>',
 'NESTOR Collective \u00e8 una comunit\u00e0 internazionale non profit che collega studenti universitari attraverso la negoziazione, la comunicazione strategica e la leadership, aprendo le porte a esperti, idee e opportunit\u00e0 straordinarie da tutto il mondo.</p>',
 'NESTOR Collective es una comunidad internacional sin fines de lucro que conecta a estudiantes universitarios a trav\u00e9s de la negociaci\u00f3n, la comunicaci\u00f3n estrat\u00e9gica y el liderazgo, y les abre las puertas a expertos, ideas y oportunidades excepcionales de todo el mundo.</p>'),
('<a class="btn btn-ghost" href="#story">Our story</a>', '<a class="btn btn-ghost" href="#story">La nostra storia</a>', '<a class="btn btn-ghost" href="#story">Nuestra historia</a>'),
('<span>Scroll</span>', '<span>Scorri</span>', '<span>Desplazar</span>'),

# ---------- 02 belief ----------
('<b>02</b> The belief', '<b>02</b> Il principio', '<b>02</b> La convicci\u00f3n'),
('<span class="we">We believe\u2026</span>', '<span class="we">Crediamo che\u2026</span>', '<span class="we">Creemos que\u2026</span>'),
('that every student interested in negotiation, strategic communication and leadership, should have access to *meaningful learning* and *networking opportunities* \u2014 regardless of their university, country or economic background.',
 'ogni studente interessato alla negoziazione, alla comunicazione strategica e alla leadership debba avere accesso a *una formazione di valore* e a *opportunit\u00e0 di networking* \u2014 indipendentemente dalla propria universit\u00e0, dal proprio paese o dalle proprie possibilit\u00e0 economiche.',
 'todo estudiante interesado en la negociaci\u00f3n, la comunicaci\u00f3n estrat\u00e9gica y el liderazgo deber\u00eda tener acceso a *formaci\u00f3n de verdad* y a *oportunidades de networking* \u2014 sin importar su universidad, su pa\u00eds ni su situaci\u00f3n econ\u00f3mica.'),
('<span>Any university</span><span>Any country</span><span>Any background</span>',
 '<span>Qualsiasi universit\u00e0</span><span>Qualsiasi paese</span><span>Qualsiasi provenienza</span>',
 '<span>Cualquier universidad</span><span>Cualquier pa\u00eds</span><span>Cualquier origen</span>'),

# ---------- 03 community ----------
('<b>03</b> The community', '<b>03</b> La comunit\u00e0', '<b>03</b> La comunidad'),
('One community.<br><b>Different paths.</b>', 'Una comunit\u00e0.<br><b>Percorsi diversi.</b>', 'Una comunidad.<br><b>Caminos distintos.</b>'),
('Students from different universities and countries, united by a shared interest in negotiation, strategic communication and leadership \u2014 and by the ambition to learn from each other.',
 'Studenti di universit\u00e0 e paesi diversi, uniti da un interesse comune per la negoziazione, la comunicazione strategica e la leadership \u2014 e dall\u2019ambizione di imparare gli uni dagli altri.',
 'Estudiantes de distintas universidades y pa\u00edses, unidos por un inter\u00e9s com\u00fan en la negociaci\u00f3n, la comunicaci\u00f3n estrat\u00e9gica y el liderazgo \u2014 y por la ambici\u00f3n de aprender unos de otros.'),
('aria-label="Interactive globe showing the cities of the NESTOR network"', 'aria-label="Globo interattivo con le citt\u00e0 della rete NESTOR"', 'aria-label="Globo interactivo con las ciudades de la red NESTOR"'),
('<div class="globe-hint">Drag to explore</div>', '<div class="globe-hint">Trascina per esplorare</div>', '<div class="globe-hint">Arrastra para explorar</div>'),
('<div class="lbl">Countries</div>', '<div class="lbl">Paesi</div>', '<div class="lbl">Pa\u00edses</div>'),
('<div class="lbl">Continents</div>', '<div class="lbl">Continenti</div>', '<div class="lbl">Continentes</div>'),
('<div class="lbl">Universities</div>', '<div class="lbl">Universit\u00e0</div>', '<div class="lbl">Universidades</div>'),
('<div class="lbl">Community</div>', '<div class="lbl">Comunit\u00e0</div>', '<div class="lbl">Comunidad</div>'),

# ---------- 04 what we do ----------
('<b>04</b> What we do', '<b>04</b> Cosa facciamo', '<b>04</b> Qu\u00e9 hacemos'),
('Learning. Networking.<br><b>Opportunities.</b>', 'Formazione. Networking.<br><b>Opportunit\u00e0.</b>', 'Formaci\u00f3n. Networking.<br><b>Oportunidades.</b>'),
('Three things every member gets from NESTOR, whatever their university or country.',
 'Tre cose che NESTOR offre a ogni membro, qualunque sia la sua universit\u00e0 o il suo paese.',
 'Tres cosas que NESTOR le da a cada miembro, sea cual sea su universidad o su pa\u00eds.'),
('<span class="k">Learning</span>', '<span class="k">Formazione</span>', '<span class="k">Formaci\u00f3n</span>'),
('<h3>Learn from people who built extraordinary careers.</h3>', '<h3>Impara da chi ha costruito carriere straordinarie.</h3>', '<h3>Aprende de quienes construyeron carreras extraordinarias.</h3>'),
('<p>Conversations, webinars and Q&amp;A sessions with negotiators, diplomats, experts and CEOs.</p>',
 '<p>Conversazioni, webinar e sessioni di Q&amp;A con negoziatori, diplomatici, esperti e CEO.</p>',
 '<p>Conversaciones, webinars y rondas de preguntas con negociadores, diplom\u00e1ticos, expertos y CEOs.</p>'),
('<h3>Connect with ambitious students across borders.</h3>', '<h3>Entra in contatto con studenti ambiziosi oltre i confini.</h3>', '<h3>Conecta con estudiantes ambiciosos de otros pa\u00edses.</h3>'),
('<p>A single community linking associations of law, consulting, diplomacy, marketing, leadership and entrepreneurship.</p>',
 '<p>Una sola comunit\u00e0 che collega associazioni di diritto, consulenza, diplomazia, marketing, leadership e imprenditorialit\u00e0.</p>',
 '<p>Una sola comunidad que conecta asociaciones de derecho, consultor\u00eda, diplomacia, marketing, liderazgo y emprendimiento.</p>'),
('<span class="k">Opportunities</span>', '<span class="k">Opportunit\u00e0</span>', '<span class="k">Oportunidades</span>'),
('<h3>Discover ways to learn, collaborate and grow.</h3>', '<h3>Scopri modi per imparare, collaborare e crescere.</h3>', '<h3>Descubre formas de aprender, colaborar y crecer.</h3>'),
('<p>Partnerships, projects and recognition for the most motivated students in the network.</p>',
 '<p>Collaborazioni, progetti e riconoscimenti per gli studenti pi\u00f9 motivati della rete.</p>',
 '<p>Alianzas, proyectos y reconocimiento para los estudiantes m\u00e1s motivados de la red.</p>'),
('programs-label">Inside NESTOR</div>', 'programs-label">Dentro NESTOR</div>', 'programs-label">Dentro de NESTOR</div>'),
('<span class="when">Always on</span>', '<span class="when">Sempre attivo</span>', '<span class="when">Siempre activo</span>'),
('<p>An international community bringing together ambitious students from different universities and countries, united by an interest in negotiation and strategic communication.</p>',
 '<p>Una comunit\u00e0 internazionale che riunisce studenti ambiziosi di universit\u00e0 e paesi diversi, uniti dall\u2019interesse per la negoziazione e la comunicazione strategica.</p>',
 '<p>Una comunidad internacional que re\u00fane a estudiantes ambiciosos de distintas universidades y pa\u00edses, unidos por el inter\u00e9s en la negociaci\u00f3n y la comunicaci\u00f3n estrat\u00e9gica.</p>'),
('<span class="when">Every month</span>', '<span class="when">Ogni mese</span>', '<span class="when">Todos los meses</span>'),
('<p>A webinar featuring internationally recognized speakers, followed by a Q&amp;A session with students from partner associations.</p>',
 '<p>Un webinar con speaker riconosciuti a livello internazionale, seguito da una sessione di Q&amp;A con studenti delle associazioni partner.</p>',
 '<p>Un webinar con speakers reconocidos internacionalmente, seguido de una ronda de preguntas con estudiantes de las asociaciones partner.</p>'),
('<span class="when">End of academic year</span>', '<span class="when">Fine dell\u2019anno accademico</span>', '<span class="when">Fin del a\u00f1o acad\u00e9mico</span>'),
("<p>The speakers' contributions and the ideas that emerged, brought together in a shared summary and a final in-person event.</p>",
 '<p>I contributi degli speaker e le idee emerse, raccolti in una sintesi condivisa e in un evento finale in presenza.</p>',
 '<p>Los aportes de los speakers y las ideas que surgieron, reunidos en un resumen compartido y un evento final presencial.</p>'),

# ---------- 05 speakers ----------
('<b>05</b> Speakers', '<b>05</b> Speaker', '<b>05</b> Speakers'),
('People worth<br><b>listening to.</b>', 'Persone che vale<br><b>la pena ascoltare.</b>', 'Personas a las que<br><b>vale la pena escuchar.</b>'),
('Experts who have shaped how the world negotiates, communicates and leads. One conversation a month, open to students from every partner association.',
 'Esperti che hanno definito il modo in cui il mondo negozia, comunica e guida. Una conversazione al mese, aperta agli studenti di tutte le associazioni partner.',
 'Expertos que marcaron la forma en que el mundo negocia, comunica y lidera. Una conversaci\u00f3n por mes, abierta a estudiantes de todas las asociaciones partner.'),
('aria-label="NESTOR speakers"', 'aria-label="Speaker di NESTOR"', 'aria-label="Speakers de NESTOR"'),
('aria-label="Choose a speaker"', 'aria-label="Scegli uno speaker"', 'aria-label="Elige un speaker"'),
('aria-label="Previous"', 'aria-label="Precedente"', 'aria-label="Anterior"'),
('aria-label="Next"', 'aria-label="Successivo"', 'aria-label="Siguiente"'),
('<span>The NESTOR Speaker Archive grows with every session</span><span>Monthly \u00b7 Global Thought Leaders</span>',
 '<span>Il NESTOR Speaker Archive cresce a ogni sessione</span><span>Ogni mese \u00b7 Global Thought Leaders</span>',
 '<span>El NESTOR Speaker Archive crece con cada sesi\u00f3n</span><span>Todos los meses \u00b7 Global Thought Leaders</span>'),
('<span class="lbl">NESTOR Speaker</span>', '<span class="lbl">Speaker NESTOR</span>', '<span class="lbl">Speaker de NESTOR</span>'),
('aria-label="Close"', 'aria-label="Chiudi"', 'aria-label="Cerrar"'),

# ---------- 06 team ----------
('<b>06</b> The people behind NESTOR', '<b>06</b> Le persone dietro NESTOR', '<b>06</b> Las personas detr\u00e1s de NESTOR'),
('Built across<br><b>borders.</b>', 'Costruito oltre<br><b>i confini.</b>', 'Construido a trav\u00e9s<br><b>de las fronteras.</b>'),
('NESTOR is built by students, for students, from Milan to San Francisco. These are some of the people making it happen.',
 'NESTOR \u00e8 costruito da studenti, per studenti, da Milano a San Francisco. Queste sono alcune delle persone che lo rendono possibile.',
 'NESTOR est\u00e1 hecho por estudiantes, para estudiantes, de Mil\u00e1n a San Francisco. Estas son algunas de las personas que lo hacen posible.'),
('aria-label="The people behind NESTOR"', 'aria-label="Le persone dietro NESTOR"', 'aria-label="Las personas detr\u00e1s de NESTOR"'),
('aria-label="Choose a person"', 'aria-label="Scegli una persona"', 'aria-label="Elige una persona"'),

# ---------- nuestra historia ----------
('<div class="sec-label rv">Our story</div>', '<div class="sec-label rv">La nostra storia</div>', '<div class="sec-label rv">Nuestra historia</div>'),
('The story<br><b>so far.</b>', 'La storia<br><b>fino a qui.</b>', 'La historia<br><b>hasta ahora.</b>'),
('<p>Simone begins a mentorship with former FBI Special Agent Joe Navarro, now recognized as one of the world\u2019s leading experts in nonverbal communication and human behavior.</p>',
 '<p>Simone inizia un percorso di mentorship con l\u2019ex agente speciale dell\u2019FBI Joe Navarro, oggi riconosciuto come uno dei maggiori esperti al mondo di comunicazione non verbale e comportamento umano.</p>',
 '<p>Simone empieza una mentor\u00eda con el ex agente especial del FBI Joe Navarro, hoy reconocido como uno de los mayores expertos del mundo en comunicaci\u00f3n no verbal y comportamiento humano.</p>'),
('<p>Simone collaborates with Giuseppe Conti and CABL, a Swiss boutique consultancy focused on negotiation training and culture for Fortune 500 companies.</p>',
 '<p>Simone collabora con Giuseppe Conti e CABL, una boutique di consulenza svizzera specializzata in formazione e cultura della negoziazione per aziende Fortune 500.</p>',
 '<p>Simone colabora con Giuseppe Conti y CABL, una consultora boutique suiza especializada en formaci\u00f3n y cultura de negociaci\u00f3n para empresas Fortune 500.</p>'),
('<p>NESTOR Collective is born: a non-profit community connecting university students across countries through negotiation, strategic communication and leadership.</p>',
 '<p>Nasce NESTOR Collective: una comunit\u00e0 non profit che collega studenti universitari di paesi diversi attraverso la negoziazione, la comunicazione strategica e la leadership.</p>',
 '<p>Nace NESTOR Collective: una comunidad sin fines de lucro que conecta a estudiantes universitarios de distintos pa\u00edses a trav\u00e9s de la negociaci\u00f3n, la comunicaci\u00f3n estrat\u00e9gica y el liderazgo.</p>'),
('<div class="yr">Today</div>', '<div class="yr">Oggi</div>', '<div class="yr">Hoy</div>'),
('<p>A growing international team, spanning 3 continents and 4 languages, is shaping the future of NESTOR Collective.</p>',
 '<p>Un team internazionale in crescita, su 3 continenti e in 4 lingue, sta costruendo il futuro di NESTOR Collective.</p>',
 '<p>Un equipo internacional en crecimiento, en 3 continentes y 4 idiomas, est\u00e1 construyendo el futuro de NESTOR Collective.</p>'),

# ---------- 07 partners ----------
('<b>07</b> Partners', '<b>07</b> Partner', '<b>07</b> Partners'),
('The network<br><b>behind the network.</b>', 'La rete<br><b>dietro la rete.</b>', 'La red<br><b>detr\u00e1s de la red.</b>'),
('Two kinds of partners with two different roles: the communities that make up the network, and the organizations that support it.',
 'Due tipi di partner con due ruoli diversi: le comunit\u00e0 che compongono la rete e le organizzazioni che la sostengono.',
 'Dos tipos de partners con dos roles distintos: las comunidades que forman la red y las organizaciones que la sostienen.'),
('<span class="kind">Community</span>', '<span class="kind">Comunit\u00e0</span>', '<span class="kind">Comunidad</span>'),
('<h3>Student associations &amp; university communities</h3>', '<h3>Associazioni studentesche e comunit\u00e0 universitarie</h3>', '<h3>Asociaciones estudiantiles y comunidades universitarias</h3>'),
('<p>The associations and university groups that are part of the NESTOR network.</p>',
 '<p>Le associazioni e i gruppi universitari che fanno parte della rete NESTOR.</p>',
 '<p>Las asociaciones y los grupos universitarios que forman parte de la red NESTOR.</p>'),
('<span class="kind">Supporters</span>', '<span class="kind">Sostenitori</span>', '<span class="kind">Quienes nos apoyan</span>'),
('<h3>Companies &amp; organizations</h3>', '<h3>Aziende e organizzazioni</h3>', '<h3>Empresas y organizaciones</h3>'),
('<p>Organizations that support NESTOR and its mission of accessible, high-level learning.</p>',
 '<p>Organizzazioni che sostengono NESTOR e la sua missione: una formazione di alto livello e accessibile.</p>',
 '<p>Organizaciones que apoyan a NESTOR y su misi\u00f3n de formaci\u00f3n de alto nivel y accesible.</p>'),
("<p>Is your association or organization interested in joining the network? We'd love to hear from you.</p>",
 '<p>La tua associazione o organizzazione vuole entrare nella rete? Ci farebbe piacere sentirti.</p>',
 '<p>\u00bfTu asociaci\u00f3n u organizaci\u00f3n quiere sumarse a la red? Nos encantar\u00eda hablar contigo.</p>'),
('>Become a partner <span class="arrow">', '>Diventa partner <span class="arrow">', '>Ser partner <span class="arrow">'),

# ---------- 08 join ----------
('<b>08</b> Join NESTOR', '<b>08</b> Unisciti a NESTOR', '<b>08</b> \u00danete a NESTOR'),
('<span class="we rv d1">Be part of the community.</span>', '<span class="we rv d1">Entra a far parte della comunit\u00e0.</span>', '<span class="we rv d1">S\u00e9 parte de la comunidad.</span>'),
("There's a seat<br>at the <b>table</b><br>for you.", 'C\u2019\u00e8 un posto<br>al <b>tavolo</b><br>per te.', 'Hay un lugar<br>en la <b>mesa</b><br>para ti.'),
("Whether you're a student, an association or an organization, there's a place for you in NESTOR. Tell us who you are and we'll get in touch.",
 'Che tu sia uno studente, un\u2019associazione o un\u2019organizzazione, in NESTOR c\u2019\u00e8 spazio per te. Raccontaci chi sei e ti contatteremo.',
 'Seas estudiante, asociaci\u00f3n u organizaci\u00f3n, en NESTOR hay un lugar para ti. Cu\u00e9ntanos qui\u00e9n eres y te escribimos.'),
('<span class="pill">Students</span><span class="pill">Student associations</span><span class="pill">Universities</span><span class="pill">Organizations</span>',
 '<span class="pill">Studenti</span><span class="pill">Associazioni studentesche</span><span class="pill">Universit\u00e0</span><span class="pill">Organizzazioni</span>',
 '<span class="pill">Estudiantes</span><span class="pill">Asociaciones estudiantiles</span><span class="pill">Universidades</span><span class="pill">Organizaciones</span>'),
('<div class="t">Request to join</div>', '<div class="t">Richiesta di adesione</div>', '<div class="t">Solicitud para sumarse</div>'),
('<label for="fName">Name</label>', '<label for="fName">Nome</label>', '<label for="fName">Nombre</label>'),
('<label for="fUni">University / organization</label>', '<label for="fUni">Universit\u00e0 / organizzazione</label>', '<label for="fUni">Universidad / organizaci\u00f3n</label>'),
('<label for="fCountry">Country</label>', '<label for="fCountry">Paese</label>', '<label for="fCountry">Pa\u00eds</label>'),
('<label for="fWho">I am a</label>', '<label for="fWho">Sono</label>', '<label for="fWho">Soy</label>'),
('<option>Student</option><option>Student association</option><option>University</option><option>Company or organization</option><option>Speaker</option>',
 '<option>Studente</option><option>Associazione studentesca</option><option>Universit\u00e0</option><option>Azienda o organizzazione</option><option>Speaker</option>',
 '<option>Estudiante</option><option>Asociaci\u00f3n estudiantil</option><option>Universidad</option><option>Empresa u organizaci\u00f3n</option><option>Speaker</option>'),
('Why NESTOR? <span style="opacity:.6;letter-spacing:0;text-transform:none">(optional)</span>',
 'Perch\u00e9 NESTOR? <span style="opacity:.6;letter-spacing:0;text-transform:none">(facoltativo)</span>',
 '\u00bfPor qu\u00e9 NESTOR? <span style="opacity:.6;letter-spacing:0;text-transform:none">(opcional)</span>'),
('>Send request <span class="arrow">', '>Invia la richiesta <span class="arrow">', '>Enviar solicitud <span class="arrow">'),
("<div class=\"note\">We'll answer personally. No newsletters, no spam.</div>",
 '<div class="note">Ti risponderemo personalmente. Niente newsletter, niente spam.</div>',
 '<div class="note">Te respondemos personalmente. Sin newsletters ni spam.</div>'),

# ---------- pie ----------
('<div class="claim">Built by students, for students. Six countries, three continents, one table.</div>',
 '<div class="claim">Costruito da studenti, per studenti. Sei paesi, tre continenti, un tavolo.</div>',
 '<div class="claim">Hecho por estudiantes, para estudiantes. Seis pa\u00edses, tres continentes, una mesa.</div>'),
('<h5>Explore</h5>', '<h5>Esplora</h5>', '<h5>Explorar</h5>'),
('<h5>Follow</h5>', '<h5>Seguici</h5>', '<h5>S\u00edguenos</h5>'),
('<li><a href="#belief">The belief</a></li>', '<li><a href="#belief">Il principio</a></li>', '<li><a href="#belief">La convicci\u00f3n</a></li>'),
('<li><a href="#join">Join NESTOR</a></li>', '<li><a href="#join">Unisciti a NESTOR</a></li>', '<li><a href="#join">\u00danete a NESTOR</a></li>'),
('<span>\u00a9 2026 NESTOR Collective \u00b7 International non-profit community</span>',
 '<span>\u00a9 2026 NESTOR Collective \u00b7 Comunit\u00e0 internazionale non profit</span>',
 '<span>\u00a9 2026 NESTOR Collective \u00b7 Comunidad internacional sin fines de lucro</span>'),
('<span>Negotiation \u00b7 Strategic communication \u00b7 Leadership \u00b7 Diplomacy</span>',
 '<span>Negoziazione \u00b7 Comunicazione strategica \u00b7 Leadership \u00b7 Diplomazia</span>',
 '<span>Negociaci\u00f3n \u00b7 Comunicaci\u00f3n estrat\u00e9gica \u00b7 Liderazgo \u00b7 Diplomacia</span>'),

# ---------- ciudades y paises (globo + equipo) ----------
("name:'Milan'", "name:'Milano'", "name:'Mil\u00e1n'"),
("city:'Milan'", "city:'Milano'", "city:'Mil\u00e1n'"),
("name:'Stockholm'", "name:'Stoccolma'", "name:'Estocolmo'"),
("city:'Stockholm'", "city:'Stoccolma'", "city:'Estocolmo'"),
("name:'Athens'", "name:'Atene'", "name:'Atenas'"),
("name:'New Delhi'", "name:'Nuova Delhi'", "name:'Nueva Delhi'"),
("city:'New Delhi'", "city:'Nuova Delhi'", "city:'Nueva Delhi'"),
("city:'Turin'", "city:'Torino'", "city:'Tur\u00edn'"),
("country:'Italy'", "country:'Italia'", "country:'Italia'"),
("country:'Sweden'", "country:'Svezia'", "country:'Suecia'"),
("country:'Greece'", "country:'Grecia'", "country:'Grecia'"),
("country:'India'", "country:'India'", "country:'India'"),

# ---------- equipo: roles y universidades ----------
("role:'Founder & Executive Director'", "role:'Fondatore e Direttore Esecutivo'", "role:'Fundador y Director Ejecutivo'"),
("role:'International Relations & Network Development'", "role:'Relazioni Internazionali e Sviluppo della Rete'", "role:'Relaciones Internacionales y Desarrollo de la Red'"),
("role:'Advisory Board'", "role:'Advisory Board'", "role:'Consejo Asesor'"),
("uni:'IULM University'", "uni:'Universit\u00e0 IULM'", "uni:'Universidad IULM'"),
("uni:'University of Turin'", "uni:'Universit\u00e0 di Torino'", "uni:'Universidad de Tur\u00edn'"),

# ---------- equipo: biografias ----------
("bio:'A student at IULM University in Milan, passionate about communication, negotiation and human behavior. Since 2024 he has been mentored by Joe Navarro, and he has collaborated with Giuseppe Conti and CABL, a Swiss boutique consultancy focused on negotiation training for Fortune 500 companies. NESTOR grew out of those experiences: connecting professional experience with the next generation.'",
 "bio:'Studente dell\u2019Universit\u00e0 IULM di Milano, appassionato di comunicazione, negoziazione e comportamento umano. Dal 2024 \u00e8 seguito come mentee da Joe Navarro e ha collaborato con Giuseppe Conti e CABL, una boutique di consulenza svizzera specializzata in formazione sulla negoziazione per aziende Fortune 500. NESTOR nasce da queste esperienze: unire l\u2019esperienza professionale alla generazione che arriva.'",
 "bio:'Estudiante de la Universidad IULM de Mil\u00e1n, apasionado por la comunicaci\u00f3n, la negociaci\u00f3n y el comportamiento humano. Desde 2024 es mentoreado por Joe Navarro y colabor\u00f3 con Giuseppe Conti y CABL, una consultora boutique suiza especializada en formaci\u00f3n en negociaci\u00f3n para empresas Fortune 500. NESTOR naci\u00f3 de esas experiencias: unir la experiencia profesional con la generaci\u00f3n que viene.'"),

("bio:'Thiago is an entrepreneur from Patagonia, Argentina. He founded a digital marketing agency at 15 and grew it to a team of six serving clients across Argentina and Chile, then co-founded a financial education project for young Argentines. He now studies Management & Technology at Tetr College of Business, a programme that moves between countries each term alongside classmates from more than 40 nationalities. At NESTOR he builds the international network \u2014 finding the people who can carry the project into new countries, and connecting them to the team.'",
 "bio:'Thiago \u00e8 un imprenditore della Patagonia, in Argentina. A 15 anni ha fondato un\u2019agenzia di marketing digitale portandola a un team di sei persone con clienti in Argentina e Cile, e ha poi co-fondato un progetto di educazione finanziaria per giovani argentini. Oggi studia Management & Technology alla Tetr College of Business, un percorso che cambia paese a ogni trimestre insieme a compagni di oltre 40 nazionalit\u00e0. In NESTOR costruisce la rete internazionale: trova le persone che possono portare il progetto in nuovi paesi e le collega al team.'",
 "bio:'Thiago es un emprendedor de la Patagonia argentina. A los 15 fund\u00f3 una agencia de marketing digital que lleg\u00f3 a un equipo de seis personas con clientes en Argentina y Chile, y despu\u00e9s co-fund\u00f3 un proyecto de educaci\u00f3n financiera para j\u00f3venes argentinos. Hoy estudia Management & Technology en Tetr College of Business, un programa que cambia de pa\u00eds cada trimestre junto a compa\u00f1eros de m\u00e1s de 40 nacionalidades. En NESTOR construye la red internacional: encuentra a las personas que pueden llevar el proyecto a nuevos pa\u00edses y las conecta con el equipo.'"),

("bio:'Originally from Varese, Italy, Alessandro is currently based in Stockholm, where he is pursuing a Bachelor\u2019s degree in Economics at the Stockholm School of Economics (SSE). His international journey has taken him to Canada and Japan, where he lived for study experiences that shaped his international perspective and interest in connecting students across borders. Alessandro is also a co-founder of the Nordics Chapter of United Italian Societies (UIS), a leading network connecting Italian students studying abroad. After previously serving in a leadership position on the network\u2019s board, he now focuses on the Nordics community as Country Manager.'",
 "bio:'Originario di Varese, Alessandro vive oggi a Stoccolma, dove sta conseguendo una laurea triennale in Economia alla Stockholm School of Economics (SSE). Il suo percorso internazionale lo ha portato in Canada e in Giappone, esperienze di studio che hanno formato il suo sguardo internazionale e l\u2019interesse a connettere studenti oltre i confini. Alessandro \u00e8 inoltre co-fondatore del Nordics Chapter di United Italian Societies (UIS), una delle principali reti di studenti italiani all\u2019estero. Dopo aver ricoperto un ruolo di leadership nel board della rete, oggi segue la comunit\u00e0 nordica come Country Manager.'",
 "bio:'Originario de Varese, Italia, Alessandro vive hoy en Estocolmo, donde cursa la licenciatura en Econom\u00eda en la Stockholm School of Economics (SSE). Su recorrido internacional lo llev\u00f3 a Canad\u00e1 y Jap\u00f3n, experiencias de estudio que formaron su mirada internacional y su inter\u00e9s por conectar estudiantes de distintos pa\u00edses. Alessandro tambi\u00e9n es co-fundador del Nordics Chapter de United Italian Societies (UIS), una de las principales redes de estudiantes italianos en el exterior. Despu\u00e9s de ocupar un rol de liderazgo en el board de la red, hoy se enfoca en la comunidad n\u00f3rdica como Country Manager.'"),

("bio:'Tommaso was born in Cuneo, Italy, and holds a Bachelor\u2019s degree in Business Administration, with a focus on business management. He is currently pursuing a Master\u2019s degree in Corporate Finance and Financial Markets at the University of Turin (UniTo). He is one of the founders of Foundy, a platform dedicated to helping young people turn their ideas into projects and startups. Alongside his academic and entrepreneurial activities, he is also involved in volunteering with children aged 8 to 12. Curious and ambitious, Tommaso is passionate about learning through new experiences, travelling and meeting people from different backgrounds and cultures. Through Foundy, he aims to support young entrepreneurs in bringing their ideas to life, while developing his own path towards becoming a local point of reference in the financial sector.'",
 "bio:'Tommaso \u00e8 nato a Cuneo e ha una laurea triennale in Economia Aziendale, con focus sulla gestione d\u2019impresa. Sta ora conseguendo una laurea magistrale in Finanza Aziendale e Mercati Finanziari all\u2019Universit\u00e0 di Torino (UniTo). \u00c8 tra i fondatori di Foundy, una piattaforma che aiuta i giovani a trasformare le proprie idee in progetti e startup. Accanto alle attivit\u00e0 accademiche e imprenditoriali, fa volontariato con bambini dagli 8 ai 12 anni. Curioso e ambizioso, Tommaso ama imparare attraverso nuove esperienze, viaggiare e incontrare persone di provenienze e culture diverse. Con Foundy vuole sostenere i giovani imprenditori nel dare vita alle loro idee, costruendo intanto il proprio percorso per diventare un punto di riferimento nel settore finanziario.'",
 "bio:'Tommaso naci\u00f3 en Cuneo, Italia, y tiene una licenciatura en Administraci\u00f3n de Empresas, con foco en gesti\u00f3n. Hoy cursa una maestr\u00eda en Finanzas Corporativas y Mercados Financieros en la Universidad de Tur\u00edn (UniTo). Es uno de los fundadores de Foundy, una plataforma dedicada a ayudar a los j\u00f3venes a convertir sus ideas en proyectos y startups. Adem\u00e1s de lo acad\u00e9mico y lo emprendedor, hace voluntariado con chicos de 8 a 12 a\u00f1os. Curioso y ambicioso, a Tommaso le apasiona aprender con experiencias nuevas, viajar y conocer personas de distintos or\u00edgenes y culturas. Con Foundy busca acompa\u00f1ar a j\u00f3venes emprendedores a dar vida a sus ideas, mientras construye su propio camino para ser una referencia en el sector financiero.'"),

("bio:'Originally from Sardinia, Italy, Mattia graduated from IULM University in Milan with a degree in Corporate Communication and Public Relations. He is currently continuing his academic journey at Universit\u00e0 Cattolica del Sacro Cuore, where he studies Markets and Business Strategies. He gained his first professional experience at TDK Italy, where he completed an internship as a Sales Assistant, gaining experience in the commercial side of an international company.'",
 "bio:'Originario della Sardegna, Mattia si \u00e8 laureato all\u2019Universit\u00e0 IULM di Milano in Comunicazione d\u2019Impresa e Relazioni Pubbliche. Prosegue oggi il suo percorso accademico all\u2019Universit\u00e0 Cattolica del Sacro Cuore, dove studia Mercati e Strategie d\u2019Impresa. La sua prima esperienza professionale \u00e8 stata in TDK Italy, con uno stage come Sales Assistant che gli ha fatto conoscere il lato commerciale di un\u2019azienda internazionale.'",
 "bio:'Originario de Cerde\u00f1a, Italia, Mattia se gradu\u00f3 en la Universidad IULM de Mil\u00e1n en Comunicaci\u00f3n Corporativa y Relaciones P\u00fablicas. Hoy contin\u00faa su camino acad\u00e9mico en la Universit\u00e0 Cattolica del Sacro Cuore, donde estudia Mercados y Estrategias de Negocio. Su primera experiencia profesional fue en TDK Italia, con una pasant\u00eda como Sales Assistant que lo acerc\u00f3 al lado comercial de una empresa internacional.'"),

("bio:'Originally from Puglia, Italy, Gianluca is currently based in San Francisco, where he has built a community of 650+ founders and international students from the ground up. He is now the creator of From _ to SF, a series exploring the stories and perspectives of Silicon Valley pioneers. Through conversations with figures such as Giacomo Marini, co-founder of Logitech, Gianluca explores the mental models, experiences and ways of thinking behind extraordinary careers and entrepreneurial journeys. Driven by curiosity and a strong entrepreneurial mindset, he is passionate about people, ideas and the systems that shape how ambitious individuals build and think.'",
 "bio:'Originario della Puglia, Gianluca vive oggi a San Francisco, dove ha costruito da zero una comunit\u00e0 di oltre 650 founder e studenti internazionali. \u00c8 il creatore di From _ to SF, una serie che racconta le storie e i punti di vista dei pionieri della Silicon Valley. Attraverso conversazioni con figure come Giacomo Marini, co-fondatore di Logitech, Gianluca esplora i modelli mentali, le esperienze e i modi di pensare dietro carriere e percorsi imprenditoriali straordinari. Mosso dalla curiosit\u00e0 e da una forte mentalit\u00e0 imprenditoriale, \u00e8 appassionato di persone, idee e dei sistemi che plasmano il modo in cui le persone ambiziose costruiscono e pensano.'",
 "bio:'Originario de Apulia, Italia, Gianluca vive hoy en San Francisco, donde construy\u00f3 desde cero una comunidad de m\u00e1s de 650 fundadores y estudiantes internacionales. Es el creador de From _ to SF, una serie que recorre las historias y las miradas de los pioneros de Silicon Valley. En conversaciones con figuras como Giacomo Marini, co-fundador de Logitech, Gianluca explora los modelos mentales, las experiencias y las formas de pensar detr\u00e1s de carreras y recorridos emprendedores extraordinarios. Movido por la curiosidad y una fuerte mentalidad emprendedora, le apasionan las personas, las ideas y los sistemas que moldean c\u00f3mo construyen y piensan los m\u00e1s ambiciosos.'"),

# ---------- plantillas del equipo ----------
("'Student at '+m.uni+' and member of the NESTOR Advisory Board.'",
 "'Studente presso '+m.uni+' e membro dell\u2019Advisory Board di NESTOR.'",
 "'Estudiante en '+m.uni+' y miembro del Consejo Asesor de NESTOR.'"),
('data-tz="${m.tz}">Local time</span>', 'data-tz="${m.tz}">Ora locale</span>', 'data-tz="${m.tz}">Hora local</span>'),
("el.textContent='Local time '+f(el.dataset.tz)", "el.textContent='Ora locale '+f(el.dataset.tz)", "el.textContent='Hora local '+f(el.dataset.tz)"),
("'Right now it\\u2019s <b>'+f('Europe/Rome')+'</b> in Milan and <b>'+f('America/Los_Angeles')+'</b> in San Francisco. Somewhere on the team, someone is always awake.'",
 "'In questo momento a Milano sono le <b>'+f('Europe/Rome')+'</b> e a San Francisco le <b>'+f('America/Los_Angeles')+'</b>. Nel team c\\u2019\u00e8 sempre qualcuno sveglio.'",
 "'Ahora mismo en Mil\u00e1n son las <b>'+f('Europe/Rome')+'</b> y en San Francisco las <b>'+f('America/Los_Angeles')+'</b>. En el equipo siempre hay alguien despierto.'"),
("'<span class=\"badge\">Founder</span>'", "'<span class=\"badge\">Fondatore</span>'", "'<span class=\"badge\">Fundador</span>'"),

# ---------- speakers (datos) ----------
("pos:'Nonverbal communications expert and former FBI special agent'",
 "pos:'Esperto di comunicazione non verbale ed ex agente speciale dell\u2019FBI'",
 "pos:'Experto en comunicaci\u00f3n no verbal y ex agente especial del FBI'"),
("short:'Recruited by the FBI at 23, he spent 25 years there as an agent and supervisor in counterintelligence and counterterrorism, where reading people became his craft.'",
 "short:'Entrato nell\u2019FBI a 23 anni, vi ha trascorso 25 anni come agente e supervisore nel controspionaggio e nell\u2019antiterrorismo, dove leggere le persone \u00e8 diventato il suo mestiere.'",
 "short:'Reclutado por el FBI a los 23, pas\u00f3 25 a\u00f1os ah\u00ed como agente y supervisor en contrainteligencia y antiterrorismo, donde leer a las personas se volvi\u00f3 su oficio.'"),
("facts:[['25','Years at the FBI'],['2003','Retired from the FBI'],['2024','Mentor to NESTOR\\u2019s founder']]",
 "facts:[['25','Anni nell\u2019FBI'],['2003','Lascia l\u2019FBI'],['2024','Mentore del fondatore di NESTOR']]",
 "facts:[['25','A\u00f1os en el FBI'],['2003','Se retira del FBI'],['2024','Mentor del fundador de NESTOR']]"),
("'Joe Navarro was approached by the FBI at just 23, making him one of the youngest agents the Bureau had ever recruited. He went on to serve for 25 years as an agent and supervisor in counterintelligence and counterterrorism.'",
 "'Joe Navarro fu contattato dall\u2019FBI a soli 23 anni, diventando uno degli agenti pi\u00f9 giovani mai reclutati dal Bureau. Vi prest\u00f2 servizio per 25 anni come agente e supervisore nel controspionaggio e nell\u2019antiterrorismo.'",
 "'A Joe Navarro lo contact\u00f3 el FBI con apenas 23 a\u00f1os, y se convirti\u00f3 en uno de los agentes m\u00e1s j\u00f3venes jam\u00e1s reclutados por el Bureau. Sirvi\u00f3 all\u00ed 25 a\u00f1os como agente y supervisor en contrainteligencia y antiterrorismo.'"),
("'It was in that work that he developed his expertise in reading nonverbal behavior, a skill that made him an effective spy-catcher and led him to train fellow agents and members of the intelligence community.'",
 "'\u00c8 in quel lavoro che ha sviluppato la sua competenza nel leggere il comportamento non verbale, un\u2019abilit\u00e0 che lo ha reso efficace nella caccia alle spie e lo ha portato a formare altri agenti e membri della comunit\u00e0 di intelligence.'",
 "'Fue en ese trabajo donde desarroll\u00f3 su pericia para leer el comportamiento no verbal, una habilidad que lo hizo eficaz cazando espias y lo llev\u00f3 a formar a otros agentes y a miembros de la comunidad de inteligencia.'".replace('espias','esp\u00edas')),
("'After retiring from the FBI in 2003, he turned to speaking and consulting for major companies around the world, and he is today considered one of the leading authorities on nonverbal communication in business. Since 2024 he has mentored NESTOR\\u2019s founder, Simone Borgogno.'",
 "'Dopo aver lasciato l\u2019FBI nel 2003, si \u00e8 dedicato a conferenze e consulenze per grandi aziende di tutto il mondo ed \u00e8 oggi considerato una delle massime autorit\u00e0 sulla comunicazione non verbale in ambito business. Dal 2024 \u00e8 mentore del fondatore di NESTOR, Simone Borgogno.'",
 "'Tras retirarse del FBI en 2003, se dedic\u00f3 a dar charlas y asesorar a grandes empresas de todo el mundo, y hoy se lo considera una de las m\u00e1ximas autoridades en comunicaci\u00f3n no verbal aplicada a los negocios. Desde 2024 es mentor del fundador de NESTOR, Simone Borgogno.'"),
("tags:['Nonverbal communication','Human behavior','Counterintelligence','Business']",
 "tags:['Comunicazione non verbale','Comportamento umano','Controspionaggio','Business']",
 "tags:['Comunicaci\u00f3n no verbal','Comportamiento humano','Contrainteligencia','Negocios']"),
("kicker:'Next session'", "kicker:'Prossima sessione'", "kicker:'Pr\u00f3xima sesi\u00f3n'"),
("desc:'A new voice every month: negotiators, diplomats, experts and CEOs, followed by an open Q&A with students from our partner associations.'",
 "desc:'Una nuova voce ogni mese: negoziatori, diplomatici, esperti e CEO, con un Q&A aperto agli studenti delle nostre associazioni partner.'",
 "desc:'Una voz nueva cada mes: negociadores, diplom\u00e1ticos, expertos y CEOs, con una ronda de preguntas abierta a los estudiantes de nuestras asociaciones partner.'"),
('<b>?</b>To be announced', '<b>?</b>Da annunciare', '<b>?</b>Por anunciar'),
('<h3 class="sl-name">Who\'s <b>next?</b></h3>', '<h3 class="sl-name">Chi sar\u00e0 il <b>prossimo?</b></h3>', '<h3 class="sl-name">\u00bfQui\u00e9n <b>sigue?</b></h3>'),
('>Get notified <span class="arrow">', '>Avvisami <span class="arrow">', '>Avisarme <span class="arrow">'),
('>Read full profile <span class="arrow">', '>Leggi il profilo <span class="arrow">', '>Ver el perfil <span class="arrow">'),
("sp=>sp.soon?'Next speaker'", "sp=>sp.soon?'Prossimo speaker'", "sp=>sp.soon?'Pr\u00f3ximo speaker'"),

# ---------- partners (datos) ----------
("fill('logosCom',PARTNERS.community,8,'Association','Join as an association');",
 "fill('logosCom',PARTNERS.community,8,'Associazione','Entra come associazione');",
 "fill('logosCom',PARTNERS.community,8,'Asociaci\u00f3n','Sumarse como asociaci\u00f3n');"),
("fill('logosSup',PARTNERS.supporters,4,'Supporter','Become a supporter');",
 "fill('logosSup',PARTNERS.supporters,4,'Sostenitore','Diventa sostenitore');",
 "fill('logosSup',PARTNERS.supporters,4,'Patrocinador','Ser patrocinador');"),

# ---------- formulario (javascript) ----------
("const body='Name: '+d.name+'\\nEmail: '+d.email+'\\nUniversity / organization: '+(d.org||'-')+'\\nCountry: '+(d.country||'-')+'\\nI am a: '+d.who+'\\n\\n'+(d.message||'');",
 "const body='Nome: '+d.name+'\\nEmail: '+d.email+'\\nUniversit\u00e0 / organizzazione: '+(d.org||'-')+'\\nPaese: '+(d.country||'-')+'\\nSono: '+d.who+'\\n\\n'+(d.message||'');",
 "const body='Nombre: '+d.name+'\\nEmail: '+d.email+'\\nUniversidad / organizaci\u00f3n: '+(d.org||'-')+'\\nPa\u00eds: '+(d.country||'-')+'\\nSoy: '+d.who+'\\n\\n'+(d.message||'');"),
("encodeURIComponent('Join Nestor - '+d.name)", "encodeURIComponent('Unisciti a NESTOR - '+d.name)", "encodeURIComponent('\u00danete a NESTOR - '+d.name)"),
("'<b>Thanks, '+d.name.split(' ')[0]+'.</b> Your request is on its way. We\\'ll get back to you personally at <b>'+d.email+'</b>.'",
 "'<b>Grazie, '+d.name.split(' ')[0]+'.</b> La tua richiesta \u00e8 partita. Ti risponderemo personalmente a <b>'+d.email+'</b>.'",
 "'<b>Gracias, '+d.name.split(' ')[0]+'.</b> Tu solicitud ya est\u00e1 en camino. Te respondemos personalmente a <b>'+d.email+'</b>.'"),
]

IDIOMAS = {'it': 1, 'es': 2}

def build(lang):
    s = open(SRC, encoding='utf-8').read()
    faltan = []
    for fila in T:
        en = fila[0]; tr = fila[IDIOMAS[lang]]
        if en not in s:
            faltan.append(en[:70]); continue
        s = s.replace(en, tr)
    if faltan:
        print('  AVISO: %d textos no se encontraron en index.html:' % len(faltan))
        for f in faltan: print('   -', f)
        return None
    # idioma del documento
    s = s.replace('<html lang="en">', '<html lang="%s">' % lang, 1)
    # canonical propio de esta version
    s = s.replace('<link rel="canonical" href="https://nestorcollective.com/">',
                  '<link rel="canonical" href="https://nestorcollective.com/%s/">' % lang, 1)
    # selector: marcar el idioma activo
    s = s.replace(' aria-current="true"', '')
    s = s.replace('hreflang="%s">' % lang, 'hreflang="%s" aria-current="true">' % lang)
    out_dir = os.path.join(ROOT, lang)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'index.html')
    open(out, 'w', encoding='utf-8').write(s)
    return out

if __name__ == '__main__':
    print('textos a traducir:', len(T))
    ok = True
    for lang in ('it', 'es'):
        out = build(lang)
        if out:
            print('  %s -> %s (%d KB)' % (lang, os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))
        else:
            ok = False
    sys.exit(0 if ok else 1)
