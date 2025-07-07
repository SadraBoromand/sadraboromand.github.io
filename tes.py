e1 = [
  'Advanced',
  'Beginner'
]
py = [
  'Machine learning',
  'Deep learning',
  'Image Processing',
  'Tensorflow / Keras',
  'Pytorch',
  'OpenCV',
  'Sci-kit learn',
  'Sci-kit Image',
  'Numpy',
  'Matplotlib',
  'Pandas',
  'Seaborn',
  'Django - Intermediate',
  'Fastapi - Beginner',
]

cs = [
  'DotNet Core',
  'Asp.Net MVC',
  'Asp.Net Web API',
  'Windows Forms',
  'EF Core',
  'Razor',
  'Microsoft Visual Studio',
  'VS Code',
  'Dependency Injection',
  'Floant API',
]

dbs = [
  'PostgreSql',
  'Sql Server',
  'SQLite',
  'PhpMyAdmin',
]

commons = [
  'Docker',
  'Git / GitHub',
  'Tailwind',
  'Bootstrap',
  'Powerpoint',
  'Word',
  'Html / CSS',
  '',
  '',
]

js = [
  'Next.js',
  'Expo',
  'React Native',
]

for i in js:
  if len(i) > 0:
    skill = f'''
    <!-- skill item -->
                <span class="border ml-1 p-2 rounded-2 fs-6">{i}</span>
                <!-- end skill item -->
    '''
    print(skill)