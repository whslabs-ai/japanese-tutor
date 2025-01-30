let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = [
      pkgs.black
      (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.openai
        python-pkgs.python-dotenv
      ]))
    ];
  }
