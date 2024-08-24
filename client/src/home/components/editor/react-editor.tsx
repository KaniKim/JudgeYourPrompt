import { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import styled from "styled-components";
import CustomToolbar from "./custom-toolbar";
import { sample } from "lodash";

const placeHolderQuote: string[] = [
  "어른들은 누구나 처음에는 어린이였다. 그러나 그것을 기억하는 어른은 별로 없다.",
  "새는 알에서 나오기 위해 투쟁한다. 알은 세계이다. 태어나려는 자는 하나의 세계를 깨뜨려야 한다. 새는 신에게로 날아간다. 그 신의 이름은 아프락사스다.",
  "부끄럼 많은 생애를 보냈습니다. 저는 인간의 삶이라는 것을 도저히 이해할 수 없습니다.",
  "'박제가 되어버린 천재' 를 아시오?",
  "국경의 긴 터널을 빠져나오자, 설국이었다",
  "바다는 비에 젖지 않는다.",
  "훌쩍 떠나온 것이 나는 얼마나 기쁜지 모른다! 친구여, 인간의 마음이란 대체 어떤 것일까!",
  "이 이야기를 읽기 전에 다시 한 번 생각해 봐.",
  "역사는 우리를 저버렸지만, 그래도 상관없다.",
];

const ResizedQuill = styled(ReactQuill)`
  .ql-container {
    min-height: 300px;
    width: 100%;
    height: 100%;
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .app .ql-container {
    border-bottom-left-radius: 0.5em;
    border-bottom-right-radius: 0.5em;
    background: #fefcfc;
  }

  .ql-editor::before {
    font-size: 15px;
    color: gray;
    align-items: center;
  }
`;

export const QuillEditor = () => {
  const [value, setValue] = useState("");
  const modules = {
    toolbar: {
      container: "#toolbar",
    },
  };
  const formats = [
    "font",
    "size",
    "bold",
    "italic",
    "underline",
    "strike",
    "color",
    "background",
    "script",
    "header",
    "blockquote",
    "code-block",
    "indent",
    "list",
    "direction",
    "align",
    "link",
    "image",
    "video",
    "formula",
  ];

  return (
    <div className="flex h-screen pt-36">
      <div className="min-w-full">
        <div className="mb-6">
          <label className="mb-2 block text-sm font-medium text-gray-900 dark:text-white"></label>
          <input
            type="text"
            placeholder="제목"
            id="default-input"
            className="block w-full border-white bg-inherit p-2.5 text-sm text-white placeholder:text-gray-400"
          />
        </div>
        <CustomToolbar />
        <ResizedQuill
          theme="snow"
          value={value}
          onChange={setValue}
          placeholder={sample<string[]>(placeHolderQuote)}
          modules={modules}
          formats={formats}
        />
      </div>
    </div>
  );
};
