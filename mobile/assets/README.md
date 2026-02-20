# 📦 Assets Folder

This folder contains app assets like images, icons, and fonts.

## 📁 Structure

```
assets/
├── images/          # App images, logos, icons
│   └── logo.txt     # Placeholder - add your images here
└── fonts/           # Custom fonts (optional)
```

## 🎨 Adding Assets

### Images:
1. Place image files in `images/` folder
2. Supported formats: PNG, JPEG, GIF, WebP
3. Use in code: `Image.asset('assets/images/your_image.png')`

### Fonts:
1. Place font files (.ttf, .otf) in `fonts/` folder
2. Update `pubspec.yaml`:
```yaml
flutter:
  fonts:
    - family: YourFont
      fonts:
        - asset: assets/fonts/YourFont-Regular.ttf
```
3. Use in code: `TextStyle(fontFamily: 'YourFont')`

## 📝 Notes

- All assets must be declared in `pubspec.yaml`
- Optimize images before adding (use TinyPNG, etc.)
- Use descriptive file names
- Keep assets organized in subfolders

## ✅ Current Status

- ✅ Folder structure created
- ✅ Configured in pubspec.yaml
- ✅ Ready for your custom assets
