import { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import styled from 'styled-components';
import CustomToolbar from './custom-toolbar';

const ResizedQull = styled(ReactQuill)`
  .ql-container {
    min-height: 300px;
    width: 100%;
    height: 100%;
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .ql-editor {
    height: 100%;
    flex: 1;
    overflow-y: auto;
    width: 100%;
  }
`;

export const QuillEditor = () => {
  const [value, setValue] = useState('');
  const modules = {
    toolbar: {
      container: '#toolbar',
    },
  };
  const formats = [
    'font',
    'size',
    'bold',
    'italic',
    'underline',
    'strike',
    'color',
    'background',
    'script',
    'header',
    'blockquote',
    'code-block',
    'indent',
    'list',
    'direction',
    'align',
    'link',
    'image',
    'video',
    'formula',
  ];

  return (
    <div className='flex h-screen pt-36'>
      <div className="min-w-full">
        <div className="mb-6">
          <label className='block mb-2 text-sm font-medium text-gray-900 dark:text-white'></label>
          <input
            type='text'
            placeholder='제목'
            id='default-input'
            className='text-white text-sm border-white block w-full p-2.5 bg-inherit placeholder-gray-400 text-white'
          />
        </div>
        <CustomToolbar />
        <ResizedQull
          theme='snow'
          value={value}
          onChange={setValue}
          placeholder={'Write something awesome...'}
          modules={modules}
          formats={formats}
        />
      </div>
    </div>
  );
};
